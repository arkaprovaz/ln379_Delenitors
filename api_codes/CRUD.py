import pyodbc
import json
import pandas as pd
from datetime import datetime

mqtt_config = "jsons/db_config.json"

with open(mqtt_config, 'r') as openfile: 
    db_config = json.load(openfile) 

table = db_config["table"]

sql_conn = pyodbc.connect(
                                DRIVER="ODBC Driver 17 for SQL Server",
                                SERVER=db_config["server"],
                                DATABASE=db_config["database"],
                                UID = db_config["user"],
                                PWD = db_config["pass"]
                                #Trusted_Connection="Yes"
                            )

def runQuery(query):
    result = pd.read_sql(query, sql_conn)
    return json.loads(result.to_json(orient='records'))

#returns last number of transactions
def device_logs(num):
    query = f"select TOP ({num}) * from {table} Order By {table}.id DESC"
    return runQuery(query)[::-1]

#print(device_logs(1))


def pushToDB(data):
    vals = (data["DID"], float(data["rf"]), float(data["wl"]), float(data["temp"]), float(data["humid"]), float(data["press"]), float(data["ws"]), data["wd"], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    query = f"INSERT INTO {table} (device_id, rainfall, water_level, temperature, humidity, pressure, wind_speed, wind_direction, timestamp) VALUES {vals}"
    cursor = sql_conn.cursor()
    row = cursor.execute(query)
    sql_conn.commit()