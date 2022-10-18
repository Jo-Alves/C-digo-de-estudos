import os
from dotenv import load_dotenv
load_dotenv()

import mysql.connector
from mysql.connector import Error

def get_string_conexao():
    return mysql.connector.connect(host=os.getenv("HOST"),
                                         database=os.getenv("DATABASE"),
                                         user=os.getenv("USER"),
                                         password=os.getenv("PASS"))
    
error = Error