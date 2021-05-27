import bot
from bot import Bot
import phoneNumberParser
import json

with open("./token.txt") as t:
    token = t.readlines()

bot = Bot(token[0].strip())
offset = ""
while True:
    js = bot.get_updates(offset)
    try:
        for item in js["result"]:
            offset = item["update_id"]
            message = bot.message
            # print necessary attributes
            print(bot.name)
            print(bot.username)
            if message == "/start":
                msg = "Hi, This is a bot, The bot helps you to parse phone numbers"\
                " from messages that has numbers and texts."\
                " This can only detect mobile phone numbers, not landline. The bot is in early"\
                " development stage and might have bugs, if you find any bug or glitches"\
                " send a message to - https://www.instagram.com/mr.monsterkoala/"
                bot.send_message(msg, bot.id)
            else:
                nums = phoneNumberParser.get_num(message)
                for num in nums:
                    msg = "call - {}\n\nwhatsapp - http://api.whatsapp.com/send?phone={}".format("91"+num, "91"+num)
                    bot.send_message(msg, bot.id)
                    print(msg)
    except:
        pass
