from dotenv import load_dotenv
import os
import mysql.connector

# Carrega as variáveis do arquivo .env
load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

print('Conexão bem-sucedida')




