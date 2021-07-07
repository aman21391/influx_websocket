import websocket
import dbconn
import settings as ss
global conn
def on_message(ws, message):
    dbconn.on_message(message,conn)


def on_close(ws, close_status_code, close_msg):
    print("### connection is closed##")



def main(symbol,interval,conn):
    conn = conn

    skt = "wss://stream.binance.com:9443/ws/" + symbol + "t@kline_" + interval
    print(skt)
    ws = websocket.WebSocketApp(skt,
                                on_message=on_message,
                                on_close=on_close)

    ws.run_forever()

