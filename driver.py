
from dbconn import getconn
import logging

logger = logging.getLogger('influx_data')
import websocket
import dbconn
import settings as ss
import threading
global conn


def on_message(ws, message):
    dbconn.on_message(message,conn)


def on_close(ws, close_status_code, close_msg):
    print("### connection is closed##")



def main(symbol,interval):

    skt = "wss://stream.binance.com:9443/ws/" + symbol + "t@kline_" + interval
    ws = websocket.WebSocketApp(skt,
                                on_message=on_message,
                                on_close=on_close)
    logger.info(f"connection to websocket is complete for {symbol} and interval {interval}")

    ws.run_forever()
if __name__ == '__main__':
    conn = getconn()
    print(conn)
    counter = 0
    thread_list = []
    for symbol in ss.symbol:
        for interval in ss.interval:
            logger.info(f'Starting a new thread for {symbol} and time interval {interval}')
            counter = counter + 1
            t = threading.Thread(target=main,args=(symbol,interval))
            thread_list.append(t)
    for thred in thread_list:
        thred.start()
    for thred in thread_list:
        thred.join()
