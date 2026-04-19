from functools import wraps
from flask import request, jsonify, current_app
import jwt

#unção wraps é fundamental para a criação de decorators bem comportados.
#Ela copia os metadados da função original, como nome, docstring, etc., para a função decorada. 
#Sem isso, todas as nossas rotas protegidas precisariam ser da mesma função decorator para a ferramenta de depuração.

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_reader = request.headers['Authorization']
            try:
                token = auth_reader.split(' ')[1]
            except IndexError:
                return jsonify({"message":"Token malformado"})
        if not token:
            return jsonify({"error":"Token não encontrado"})
        try:
            data = jwt.decode(token, 
                              current_app.config['SECRET_KEY'],
                              algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({"error":"Token Expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error":"Token inválido"}), 401
        
        return f(data, *args, **kwargs)
    
    return decorated
    