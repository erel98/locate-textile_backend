from DBManager import DBManager
from src.location_properties_pkg import LocationHandler

class TransactionHandler:
    # Group transactions with respect to product id's
    def groupTransactions(self):
        dbManager = DBManager()
        transactions = dbManager.select_all('transactions', 'us-east-1') 
        # print(transactions)
        covered_ids = []
        group = {}
        
        for tx in transactions:
            # print('looking for id {}'.format(tx['product_id']))
            if covered_ids.count(tx['product_id']) == 0:
                # print('id={} does not exist in covered ids'.format(tx['product_id']))
                covered_ids.append(tx['product_id'])
                for tx2 in transactions:
                    if tx2['product_id'] == tx['product_id']:
                        try:
                            group[tx['product_id']].append({
                                'latitude': tx2['latitude'],
                                'longitude': tx2['longitude']
                            })
                        except KeyError:
                            group[tx['product_id']] = []
                            group[tx['product_id']].append({
                                'latitude': tx2['latitude'],
                                'longitude': tx2['longitude']
                            })
     
        avg_group = {}
        
        for key in group:
            count = 0
            lat = 0
            lon = 0
            for i,coord in enumerate(group[key]):
               count += 1
               lat += float(coord['latitude'])
               lon += float(coord['longitude'])
                
            avg_group[key] = {
                'latitude': lat/count,
                'longitude': lon/count,
            }
        # print(avg_group)
        return avg_group
        
    # Sort the grouped transactions with respect to the user's location
    def sortGroupedTransactionCoordinates(self, lat, lon, coords):
        locationHandler = LocationHandler.LocationHandler()
        sorted_coords = {}
        for key in coords:
            distance = locationHandler.calculateDistanceInKM(lat, lon, coords[key]['latitude'], coords[key]['longitude'])
            sorted_coords[key] = distance
        sorted_coords = dict(sorted(sorted_coords.items(), key=lambda x:x[1]))
        return sorted_coords.keys()
        
    def prepareSortedProductsResponse(self, sorted_ids):
        dbManager = DBManager()
        response_object = []
        
        products = dbManager.select_all('products','us-east-1')

        for id in sorted_ids:
            key_info={
                "id": id
            }
            product = dbManager.get_an_item('us-east-1', 'products', key_info)
            
            response_object.append(product)
        
        # in case there are some missing product transactions
        difference = [i for i in response_object if i not in products] \
      + [j for j in products if j not in response_object]
        response_object.extend(difference)
        
        return response_object
            