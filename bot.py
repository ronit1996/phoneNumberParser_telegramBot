import requests
import json
import phoneNumberParser

class Bot():
    def __init__(self, token):
        self.baseUrl = "https://api.telegram.org/bot{}/".format(token)
        self.message = ""
        self.id = 0
        self.name = ""
        self.command = False

    def get_updates(self, offset=None):
        url = self.baseUrl + "getUpdates?timeout=10"
        if offset:
            r = requests.get(url + "&offset={}".format(offset+1))
        else:
            r = requests.get(url)
        data = json.loads(r.content)

        for item in data["result"]:
            try:
                self.message = item['message']["text"]
                self.id = item["message"]["from"]["id"]
                self.name = item["message"]["from"]["first_name"]
            except:
                pass
        return data

    def send_message(self, msg, chat_id):
        msg_url = self.baseUrl + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(msg_url)



token = "1840024286:AAGD8qZ3oBFv5tQ0-LVLYoZ0gPKm3BjWw34"
bot = Bot(token)
offset = ""
while True:
    js = bot.get_updates(offset)

    for item in js["result"]:
        offset = item["update_id"]
        try:
            message = bot.message
            nums = phoneNumberParser.get_num(message)
            for num in nums:
                msg = "call - {}\n\nwhatsapp - http://api.whatsapp.com/send?phone={}".format("91"+num, "91"+num)
                bot.send_message(msg, bot.id)
        except:
            pass
