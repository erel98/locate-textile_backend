from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from DBManager import DBManager
import boto3
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user


app = Flask(__name__)
CORS(app, resources=r'/*')
db = DBManager()
region = 'us-east-1'

# Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return None

@app.route('/products', methods=['GET', 'POST'])
def get_products():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        new_product = {
            'id': post_data.get('id'),
            'name': post_data.get('name'),
            'description': post_data.get('description'),
            'image': post_data.get('image'),
            'price': post_data.get('price'),
        } 

        db.store_an_item(region, 'products', new_product)
        response_object['message'] = 'Product added!'
    else:
        response_object['products'] = db.select_all('products', region)
    return jsonify(response_object)


@app.route('/products/<id>', methods=['GET'])
def get_product_by_id(id):
    key_info={
        "id": id
    }
    product = db.get_an_item(region, 'products', key_info)
    
    if product is not None:
        print("not none")
        response = jsonify({
            'status': 'success',
            'product': product
        })
    else:
        print("none")
        response = jsonify({
            'status': 'false',
            'message': 'product not found'
        })
    print(response)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')
    