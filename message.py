import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import json
import time
import random

token = "78c65e518b0d2461106e05346524dfadc04cf41d48eee989812a899b68fe3aef35e7b6b6839d501a753ea"

vk = vk_api.VkApi(token=token)
vk._auth_token()

def vk_send(out):
    vk.method("messages.send", {"peer_id": 281346213, "message": out, "random_id": random.randint(1, 2147483647)})