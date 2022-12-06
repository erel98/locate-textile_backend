from S3Manager import S3Manager

class S3Bucketseed:
    def createProductImagesBucket(self):
        s3Manager = S3Manager()
        s3Manager.create_bucket('x21245312-products')
        
    def seedProductImagesBucket(self):
        s3Manager = S3Manager()
        
        s3Manager.upload_file('./product_files/product_1.jpg', 'x21245312-products', '1')
        s3Manager.upload_file('./product_files/product_2.jpeg', 'x21245312-products', '2')
        s3Manager.upload_file('./product_files/product_3.webp', 'x21245312-products', '3')
        s3Manager.upload_file('./product_files/product_4.jpeg', 'x21245312-products', '4')
        s3Manager.upload_file('./product_files/product_5.jpeg', 'x21245312-products', '5')
        
def main():
    seeder = S3Bucketseed()
    # create the bucket for the first time
    # seeder.createProductImagesBucket()
    # upload the product images
    # seeder.seedProductImagesBucket()
    
if __name__ == '__main__':
    main()