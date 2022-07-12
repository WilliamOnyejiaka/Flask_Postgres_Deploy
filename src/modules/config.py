from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.environ.get('HOST','')
DBNAME = os.environ.get('DBNAME','')
USER = os.environ.get('USER','')
PASSWORD = os.environ.get('PASSWORD','')
PORT = os.environ.get('DBPORT','')