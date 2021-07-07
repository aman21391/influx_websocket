from influxdb import InfluxDBClient
import settings as s
import datetime
import logging

logger = logging.getLogger('influx_data')
class Influ:
    def __init__(self,username,password,database):
        self.database = database
        self.username = username
        self.password = password
    def create_conn(self):
        self.host = s.host
        self.port = s.port
        try:
            self.conn = InfluxDBClient(self.host, self.port, self.username, self.password, self.database)
            logger.info("DB connection is successful")
        except Exception as E:
            logger.error("DB connection failed")
            print(E)
        return self.conn

def getconn():

    obj = Influ(username=s.username,password=s.password,database=s.database)
    conn = obj.create_conn()
    return conn
def on_message(message,conn):
    try:
        message = message.replace('false','0').replace('true','1')
        message = eval(message)
        logger.info(message)
    except Exception as E:
        print(E)
    if(str(message["k"]["x"])=='1'):
        son_body = [
            {
                "measurement": "crypto",
                "tags": {
                    "crypto": message["s"],
                    "interval": message["k"]["i"]
                },
                "time":datetime.datetime.fromtimestamp(message["k"]["T"]),
                "fields":{
                    "open": message["k"]["o"],
                    "close":message["k"]["c"],
                    "low":message["k"]["l"],
                    "high":message["k"]["h"],
                    "volume":message["k"]["v"]
            }}]
        try:
            conn.write_points(son_body)
            logger.info("data written on influx db")
        except Exception as E:
            print(E)
            logger.info("data written on influx db")



