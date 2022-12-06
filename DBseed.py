from DBManager import DBManager
import bcrypt

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
            'price': 100
        }
        
        d.store_an_item(region, table_name, item)
        
        item = {
            'id': '2',
            'name': 'Sweatshirt',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'price': 235
        }
        
        d.store_an_item(region, table_name, item)
        
        item = {
            'id': '3',
            'name': 'Sweater',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'price': 60
        }
        
        d.store_an_item(region, table_name, item)
        
        item = {
            'id': '4',
            'name': 'Shirt',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'price': 75
        }
        
        d.store_an_item(region, table_name, item)
        
        item = {
            'id': '5',
            'name': 'Jeans',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'price': 120
        }
        
        d.store_an_item(region, table_name, item)

    def createUsersTable(self):
        region = 'us-east-1'
        d = DBManager()
        
        table_name="users"
        
        key_schema=[
            {
                "AttributeName": "email",
                "KeyType": "HASH"
            }
        ]
        
        attribute_definitions=[
            {
                "AttributeName": "email",
                "AttributeType": "S"
            }
            
        ]
        
        provisioned_throughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
        
        d.create_table(table_name, key_schema, attribute_definitions, provisioned_throughput, region)
    
    def seedUsersTable(self):
        region = 'us-east-1'
        d = DBManager()
        
        table_name="users"
        password = bcrypt.hashpw(b'test123', bcrypt.gensalt())
        item = {
            'id': '1',
            'fullName': 'Erel Ozturk',
            'mobile': '0831104840',
            'latitude': '53.3535671',
            'longitude': '-6.250112',
            'username': 'erel98',
            'email': 'erelozturk98@gmail.com',
            'password': password
        }
        
        d.store_an_item(region, table_name, item)
        
    def createTransactionsTable(self):
        region = 'us-east-1'
        d = DBManager()
        
        table_name="transactions"
        
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
    
    # create the users table for the first time
    # dbseed.createUsersTable()
    
    # populate the users table for the first time
    # dbseed.seedUsersTable()
    
    # create the transactions table for the first time
    # dbseed.createTransactionsTable()
    
if __name__ == '__main__':
    main()