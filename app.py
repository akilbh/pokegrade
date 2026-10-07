import mysql.connector
from pymongo import MongoClient


connection = mysql.connector.connect(
    host="10.150.16.50",
    port=3306,
    user="DSKI25A1_User23",
    password="s%xMVmjakl8N5p",
    database="DSKI25A1_User23_pokegrade",
)

client = MongoClient(
    host="10.150.16.50",
    port=27017,
    username="DSKI25A1_DB_User15",
    password="kyLeFcjydJz8"
)

db = client["DSKI25A1_DB_User15"]