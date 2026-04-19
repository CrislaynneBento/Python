from flask import Blueprint, jsonify, request
from app.models.user import LoginPayLoad
from pydantic import ValidationError   
from app import db
from bson import ObjectId
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

    if user_data.username == 'admin' and user_data.password == 123:
        return jsonify({"message": "Login bem sucedido!"}), 200
    else:
        return jsonify({"message": "Credenciais inválidas"})




#----------------------------------------ROTAS DE PRODUTOS-----------------------------------------

@main_bp.route('/products', methods=['GET'])
def get_products():
    products_list = []
    productsCursor = db.products.find({})

    for product in productsCursor:
        product['_id'] = str(product['_id'])
        products_list.append(product)
        
    return jsonify(products_list)



@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({"message":"Welcome to route for append new product!"})



@main_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return jsonify({"message":f"This route returns a view of detail of id product {product_id}."})



@main_bp.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return jsonify({"message":f"This route returns a update un product with id {product_id}."})



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


