import requests
import json


class Bot():
    def __init__(self, token):
        self.baseUrl = "https://api.telegram.org/bot{}/".format(token)
        self.message = ""
        self.id = 0
        self.name = ""
        self.command = False

    def get_updates(self, offset=None):
        url = self.baseUrl + "getUpdates?timeout=100"
        if offset:
            r = requests.get(url + "&offset={}".format(offset+1))
        else:
            r = requests.get(url)
        data = json.loads(r.content)

        for item in data["result"]:
            self.message = item['message']["text"]
            self.id = item["message"]["from"]["id"]
            self.name = item["message"]["from"]["first_name"]

        return data

    def send_message(self, msg, chat_id):
        msg_url = self.baseUrl + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(msg_url)
