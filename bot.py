import requests
import time

TOKEN = "8752738010:AAFXVnStXvqsy6TJK3gkN3bbBBG7i2GvcOY"
URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates(offset=None):
    res = requests.get(URL + "getUpdates", params={"offset": offset, "timeout": 100})
    return res.json()

def send_message(chat_id, text):
    requests.post(URL + "sendMessage", data={"chat_id": chat_id, "text": text})

offset = None
while True:
    data = get_updates(offset)
    for item in data["result"]:
        offset = item["update_id"] + 1
        if "message" in item:
            chat_id = item["message"]["chat"]["id"]
            text = item["message"].get("text", "")
            
            if "မင်္ဂလာပါ" in text:
                reply = "မင်္ဂလာပါ 👋"
            else:
                reply = "Hello 😄"
                
            send_message(chat_id, reply)
    time.sleep(1)
