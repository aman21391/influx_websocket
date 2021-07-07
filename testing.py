import settings as s
from influxdb import InfluxDBClient

try:
    conn = InfluxDBClient(s.host, s.port, s.username, s.password, s.database)
except Exception as E:
    print(E)
son_body = [{
	"measurement": "btcusd_aman_1",
	"tags": {
		"user": "Aman",
		"interval": "1m"
	},
	"fields": {
		"e": "kline",
		"E": 1624876003338,
		"s": "BTCUSDT",
		"k": {
			"t": 1624875960000,
			"T": 1624876019999,
			"s": "BTCUSDT",
			"i": "1m",
			"f": 936486616,
			"L": 936488364,
			"o": "34044.71000000",
			"c": "34001.01000000",
			"h": "34055.00000000",
			"l": "34001.00000000",
			"v": "107.50280500",
			"n": 1749,
			"x": 0,
			"q": "3658172.60796940",
			"V": "47.32388000",
			"Q": "1610495.03283620",
			"B": "0"
		}
	}
}]
# try:
#     conn.write_points(son_body)
# except Exception as E:
#      print(E)
try:
    results = conn.query(f'select * from {s.symbol[0]}_aman_1')
except Exception as E:
    print(E)
print(results.raw)
points = results.get_points(tags={'user':'testing'})
for point in points:
   print(point['time'], point['duration'])