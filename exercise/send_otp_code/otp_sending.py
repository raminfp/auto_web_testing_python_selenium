import json
import time

import requests


url = "https://api.sharifict.ir/api/Authentication/SendCode"

header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7,fr;q=0.6",
    "apikey": "73076aef-6f7d-4d83-80cb-978194e9ee02",
    "Content-Length": "29",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "api.sharifict.ir",
    "Origin": "https://sharifict.ir",
    "Referer": "https://sharifict.ir/",
    "sec-ch-ua": '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}


data = { "phoneNumber": "09191583239"}

while True:
    my_req = requests.post(url, json.dumps(data), headers=header)
    if my_req:
        print("Send code")

    print("Please wait ...")
    time.sleep(10)

