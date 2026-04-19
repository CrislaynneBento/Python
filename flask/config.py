import os 
from dotenv import load_dotenv


load_dotenv()
#A função load_dotenv será responsável por ler o arquivo .env e carregar as variáveis definidas nele, 
#tornando-as acessíveis ao nosso código Python

class Config:
    MONGO_URI = os.getenv('MONGO_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
