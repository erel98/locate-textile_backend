from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from DBManager import DBManager
import boto3
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
import bcrypt


application = Flask(__name__)
CORS(application, resources=r'/*')
db = DBManager()
region = 'us-east-1'

# Setup the Flask-JWT-Extended extension
application.config["JWT_SECRET_KEY"] = "Merhaba, benim adım Erel"  # Change this!
jwt = JWTManager(application)

@application.route("/login", methods=["POST"])
def login():
    post_data = request.get_json()
    email = post_data.get("email")
    password = post_data.get("password").encode('utf-8')
    print("requested email: ",email)
    key_info={
        "email": email
    }
    user = db.get_an_item(region, 'users', key_info)
    
    if user is None:
        return jsonify({"msg": "Incorrect login credentials"}), 401
    else:
        if not bcrypt.checkpw(password, bytes(user['password'])):
            return jsonify({"msg": "Incorrect login credentials"}), 401
        
    access_token = create_access_token(identity=email)
    # save to db
    return jsonify(access_token=access_token)

@application.route('/products', methods=['GET', 'POST'])
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


@application.route('/products/<id>', methods=['GET'])
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
    application.run()
    