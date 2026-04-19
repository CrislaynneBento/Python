from flask import Blueprint, jsonify, request, current_app
from app.models.user import LoginPayLoad
from pydantic import ValidationError   
from app import db
from bson import ObjectId
from app.models.products import *
from app.decorators import token_required
from datetime import datetime, timedelta, timezone
import jwt

#blueprint é um mini app que servira como decorator para definir rotas por funcionalidade
main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return jsonify({"message":"Welcome to Framework Flask!"})



@main_bp.route('/login', methods=['POST'])
def login():
    try:

        raw_data = request.get_json()    
        user_data = LoginPayLoad(**raw_data) 
        #operador **, que desacopla o dicionário em argumentos de palavras-chave atribuídos automaticamente aos atributos de classe.
        
    except ValidationError as e: 
        return jsonify({"error": e.errors()}), 400
    
    except Exception as e: 
        return jsonify({"error": "Erro durante a requisição do dado"}), 500

    if user_data.username == 'admin' and user_data.password == "supersecret":
        token = jwt.encode(
            {
            "user_id" : user_data.username,
            "exp" : datetime.now(timezone.utc) + timedelta(minutes=30)
            },
            current_app.config['SECRET_KEY'],
            algorithm = 'HS256'
            )
        
        return jsonify({"access_token" : token}), 200
    
    return jsonify({"message": "Credenciais inválidas"}), 401




#----------------------------------------ROTAS DE PRODUTOS-----------------------------------------

@main_bp.route('/products', methods=['GET'])
def get_products(): 
    
    productsCursor = db.products.find({})
    products_list = [ProductDBModel(**product).model_dump(by_alias = True, exclude_none = True) for product in productsCursor]
    return jsonify(products_list)



@main_bp.route('/products', methods=['POST']) 
@token_required
def create_product(token):
    try: 
        product = Product(**request.get_json())
    except ValidationError as e:
        return jsonify({"Error" : e.errors()})
    
    result = db.products.insert_one(product.model_dump())
    return jsonify({"message":"Welcome to route for append new product!",
                    "id":str(result.inserted_id)}), 201



@main_bp.route('/product/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try: 
        oid = ObjectId(product_id)
        
    except Exception as e:
        return jsonify({"error" : f" Erro ao transformar o {product_id} em ObjectID: {e}!"})
    
    product = db.products.find_one({"_id": oid})

    if product:
        product_model = ProductDBModel(**product).model_dump(by_alias=True, exclude_none= True)
        return jsonify (product_model)
    else: 
        return jsonify({"error": f"produto com id: {product_id} - não encontrado"})




@main_bp.route('/product/<string:product_id>', methods=['PUT'])
@token_required
def update_product(token, product_id):
    try:
       oid = ObjectId(product_id)
       update_data = update_products(**request.get_json())
       update_result = db.products.update_one(
           
               {"_id" : oid},
               {"$set": update_data.model_dump(exclude_unset=True)}
           
       )
       if update_result.matched_count == 0:
           return jsonify({"error":"Produto não encontrado!"}), 404
       update_product = db.products.find_one({"_id":oid})
       return jsonify(ProductDBModel(**update_product).model_dump(by_alias=True, exclude_none=True))
    except ValidationError as e:
        return jsonify({"error": e.erros()})
    



@main_bp.route('/product/<int:product_id>', methods=['PUT'])
def delete_product(product_id):
    return jsonify({"message":f"This route delete a product with your id {product_id}."})



#-----------------------------------------ROTA DE VENDAS--------------------------------------------
@main_bp.route('/vendas/upload', methods=['GET'])
def upload_sales_page():
    return jsonify({"message":"Mostra as vendas da página!"})



@main_bp.route('/vendas/upload', methods=['POST'])
def upload_sales():
    return jsonify({"message":"Faz a importação de vendas através de um arquivo!"})


