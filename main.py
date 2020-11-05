token = "not for this"

import summ
import date as d
import sub
import register as reg

import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import json
import random

def get_button(label, color, payload=""):
	return {
	"action":{
		"type"   : "text",
		"payload": json.dumps(payload),
		"label"  : label},
		"color"  : color
		}


keyboard = {
	"one_time" : False,
	"buttons" : [
	[get_button ("Сумма всех моих трат", "negative")]	
	]
}


keyboard = json.dumps(keyboard, ensure_ascii = False).encode("utf-8")
keyboard = str(keyboard.decode("utf-8"))

vk = vk_api.VkApi(token=token)
vk._auth_token()

while True:

	messages = vk.method("messages.getConversations", {"offset": 0,"count" : 20, "filter": "unanswered"})

	if messages["count"] >= 1:
		
		idd = messages["items"][0]["last_message"]["from_id"]
		message = messages["items"][0]["last_message"]["text"]

		if sub.check(idd) == True:

			vk.method("messages.send", {"peer_id": idd, "message": "!","random_id": random.randint(1, 2147483647), "keyboard":keyboard})

			if message == "Сумма всех моих трат":
				output = summ.summ(idd)
				vk.method("messages.send", {"peer_id": idd, "message": F"{output} - столько денег вы потратили за месяц","random_id": random.randint(1, 2147483647)})


			elif len(message.split(" ")) == 2:
				messag = d.check_date(messages["items"][0]["last_message"]["text"], messages["items"][0]["last_message"]["from_id"])
				vk.method("messages.send", {"peer_id": idd, "message": messag,"random_id": random.randint(1, 2147483647)})

			else:
				vk.method("messages.send", {"peer_id": idd, "message": "Запишите трату в формате [вещь] [сумма]","random_id": random.randint(1, 2147483647)})


		elif sub.check(idd) == False:
			reg.reg(idd)
			vk.method("messages.send", {"peer_id": idd, "message": "Вы успешно зарегистрировались в программе!","random_id": random.randint(1, 2147483647)})
