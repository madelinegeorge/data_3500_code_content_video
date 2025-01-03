import requests
import json
import time
from datetime import datetime, timedelta


url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=12-06-2023&localization=false"
req = requests.get(url)
print(req.text)

input()

url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

key1 = 'market_data'
key2 = 'current_price'
key3 = 'usd'

dt = datetime(2022, 6, 12)

coins = ["ripple", "bitcoin-cash", "ripple", "eos", "litecoin", "ethereum", "bitcoin"]
for coin in coins:
    for i in range(364):
        dt += timedelta(days=1)
        dts = dt.strftime("%d-%m-%Y")
        url = url1 + coin + url2 + dts + url3
        req = requests.get(url)
        time.sleep(1)
        d = json.loads(req.text)
        try:
            print(dts, d[key1][key2][key3])
        except:
            print(d)