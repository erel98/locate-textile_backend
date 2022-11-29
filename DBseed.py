from DBManager import DBManager

class DBseed:
    
    def createProductsTable(self):
        region = 'us-east-1'
        d = DBManager()
        
        table_name="products"
        
        key_schema=[
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            }
        ]
        
        attribute_definitions=[
            {
                "AttributeName": "id",
                "AttributeType": "S"
            }
            
        ]
        
        provisioned_throughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
        
        d.create_table(table_name, key_schema, attribute_definitions, provisioned_throughput, region)

    def populateProductsTable(self):
        d = DBManager()
        region = 'us-east-1'
        table_name="products"
        
        item = {
            "id": "1",
            "name": "Hoodie",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'image': 'https://t3.ftcdn.net/jpg/03/53/99/46/360_F_353994605_tTu6Woyi4DSJ8BbDO2Uloyway3yWUlCE.jpg',
            'price': 100
        }
        
        d.store_an_item(region, table_name, item)
        
        item = {
            'id': '2',
            'name': 'Sweatshirt',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'image': 'https://thumbs.dreamstime.com/b/white-hoodie-mock-up-blank-sweatshirt-front-back-view-isolated-plain-mockup-hoody-design-presentation-jumper-print-158606489.jpg',
            'price': 235
        }
        
        d.store_an_item(region, table_name, item)
        
        item = {
            'id': '3',
            'name': 'Sweater',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'image': 'https://media.gq.com/photos/5bec609f28f2bf777657ff0d/1:1/w_1333,h_1333,c_limit/Mock-Neck-Sweaters-GQ-11142018_3x2.jpg',
            'price': 60
        }
        
        d.store_an_item(region, table_name, item)
        
        item = {
            'id': '4',
            'name': 'Shirt',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'image': 'https://images.squarespace-cdn.com/content/v1/528f8b33e4b01f2a315145b2/1492094615373-S6Y95SFIP6OVXKFH6BLB/t-shirt-mannequin_Front.jpg?format=1500w',
            'price': 75
        }
        
        d.store_an_item(region, table_name, item)
        
        item = {
            'id': '5',
            'name': 'Jeans',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'image': 'https://media.istockphoto.com/photos/pair-of-blue-jeans-picture-id537816451?k=20&m=537816451&s=612x612&w=0&h=N6eOnh680UXrICn9gUE6grWkfVaHButP2F-SKZLyR8c=',
            'price': 120
        }
        
        d.store_an_item(region, table_name, item)

        def createUsersTable(self):
            region = 'us-east-1'
            d = DBManager()
            
            table_name="users"
            
            key_schema=[
                {
                    "AttributeName": "id",
                    "KeyType": "HASH"
                }
            ]
            
            attribute_definitions=[
                {
                    "AttributeName": "id",
                    "AttributeType": "S"
                }
                
            ]
            
            provisioned_throughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            }
            
            d.create_table(table_name, key_schema, attribute_definitions, provisioned_throughput, region)
            

def main():
    dbseed = DBseed()
    
    # create the products table for the first time
    # dbseed.createProductsTable()
    # populate the products table for the first time
    # dbseed.populateProductsTable()
    
if __name__ == '__main__':
    main()