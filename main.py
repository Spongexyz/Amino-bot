import os
from gtts import gTTS
import urllib
import time
import requests
import json
from random import randrange
import random
from BotAmino import BotAmino, Parameters
from BotAmino import *
#logins

email = ""
password = ""
client = BotAmino(email, password)
client.wait = 2
client.prefix = "/"
client.self_callable = False


# You can do that or use os library os.listdir(path)
memes = ["MEME 1", "MEME 2"]


def vip(args):
    return args.authorId in ('your id', 'Your friend id')

@client.command("music")
def music(data):
    ms = "Converting can take up to 5 minutes"
    if data.message == '1':
        data.subClient.send_message(chatId=data.chatId, message=ms)
        with open('1.mp3', 'rb') as file:
            data.subClient.send_message(data.chatId, file=file, fileType="audio")
    elif data.message == '2':
        data.subClient.send_message(chatId=data.chatId, message=ms)
        with open('2.mp3', 'rb') as file:
            data.subClient.send_message(data.chatId, file=file, fileType="audio")
    elif data.message == '3':
        data.subClient.send_message(chatId=data.chatId, message=ms)
        with open('3.mp3', 'rb') as file:
            data.subClient.send_message(data.chatId, file=file, fileType="audio")
    elif data.message == '4':
        data.subClient.send_message(chatId=data.chatId, message=ms)
        with open('4.mp3', 'rb') as file:
            data.subClient.send_message(data.chatId, file=file, fileType="audio")
    elif data.message == '5':
        data.subClient.send_message(chatId=data.chatId, message=ms)
        with open('5.mp3', 'rb') as file:
            data.subClient.send_message(data.chatId, file=file, fileType="audio")
    elif data.message == '6':
        data.subClient.send_message(chatId=data.chatId, message=ms)
        with open('6.mp3', 'rb') as file:
            data.subClient.send_message(data.chatId, file=file, fileType="audio")
    elif data.message == '7':
        data.subClient.send_message(chatId=data.chatId, message=ms)
        with open('7.mp3', 'rb') as file:
            data.subClient.send_message(data.chatId, file=file, fileType="audio")
    elif data.message == '8':
        data.subClient.send_message(chatId=data.chatId, message=ms)
        with open('8.mp3', 'rb') as file:
            data.subClient.send_message(data.chatId, file=file, fileType="audio")
    else:
        data.subClient.send_message(chatId=data.chatId,message="[BC]Music list\n[IC] 1 - wellerman\n[IC] 2 - Yankee Doodle\n[IC] 3 - GhostFace playa Why not\n[IC] 4 - Drip of japanese emperor\n[IC] 5 - GRAVECHILL - Twighlight\n[IC] 6 - KSLV Dynamic\n[IC] 7 - us3ll3ss x Ne Skazhu  Useless weaponry\n[IC] 8 - Ciężkie czasy legionera")

@client.command("voice")
def voice(data):
    tts = gTTS(text=data.message, lang='ar', slow=False)
    tts.save('hello.mp3')
    with open("hello.mp3", "rb") as aud:
        data.subClient.send_message(data.chatId, file=aud, fileType="audio")
@client.command("name",condition=vip)
def name(data):
    data.subClient.edit_profile(nickname=data.message)
    data.subClient.send_message(chatId=data.chatId, message=f"Changed name to {data.message}")
@client.command("wall", condition=vip)
def wel(data):
    data.subClient.set_welcome_message(data.message)
    data.subClient.send_message(data.chatId,"welcome message changed")
@client.command("person")
def person(data):
    req = requests.get('https://thispersondoesnotexist.com/image')
    with open('this.png', 'wb') as file:
        file.write(req.content)
    with open('this.png', 'rb') as file:
        data.subClient.send_message(file=file, fileType="image", chatId=data.chatId)
@client.command("ask")
def ask(data):
    link = f"http://api.brainshop.ai/get?bid=153868&key=rcKonOgrUFmn5usX&uid=1&msg={data.message}"
    response = requests.get(link)
    json_data = json.loads(response.text)
    chatbot = json_data["cnt"]
    data.subClient.send_message(chatId=data.chatId,message=f"{chatbot}", replyTo=data.messageId)
@client.command("dance")
def dance(data):
    data.subClient.send_message(chatId=data.chatId,message="~(˘▾˘~) ~(˘▾˘)~ (~˘▾˘)~")
@client.command("meme")
def mem(data):
    with open(random.choice(memes), "rb") as file:
        data.subClient.send_message(file=file,fileType="image",chatId=data.chatId)

@client.on_member_leave_chat()
def say_goodbye(data: Parameters):
    data.subClient.send_message(data.chatId, f"{data.author} has left the chat")
@client.on_member_join_chat()
def say_hello(data: Parameters):
    data.subClient.send_message(data.chatId, f"{data.author} منور")

@client.command("ping")
def pong(data):
    data.subClient.send_message(chatId=data.chatId, message="pong!")
@client.command("coins")
def c(data):
    data.subClient.send_message(chatId=data.chatId, message="جميع التبرعات تذهب عبد الرحمن تعويضا عن فقدانه 264 قرش")
    coins = data.subClient.get_wallet_amount()
    data.subClient.send_message(chatId=data.chatId,message="I have: "+str(coins))
@client.command("join")
def a(data, l:str):
    if l in "https://aminoapps/p" or "http://aminoapps/p":
        data.subClient.join_chatroom(l)
        data.subClient.send_message(chatId=data.chatId, message="Joined the chatroom")
    else:
        data.subClient.send_message(chatId=data.chatId,message="Link not in amino")
@client.command("howgay")
def gay(data):

    # Use that OR use randrange
    perc = ["100%", "1%", "200%", "54%", "20%", "56%", "90%", "99.99%", "not", "30%", "21%", "19%", "18%", "17%", "16%", "15%", "14%", "13%", "12%", "11%", "10%", "9%", "8%", "7%", "6%", "5%", "4%", "3%", "2%", "22%", "23%", "24%", "25%", "26%", "27%", "28%", "29%", "30%", "31%", "32%", "33%", "34%", "35%", "36%", "37%", "38%", "39%", "40%", "41%", "42%", "43%", "44%", "45%", "46%", "47%", "48%", "49%", "50%", "51%", "52%", "53%", "55%", "56%", "57%", "58%", "59%", "60%", "61%", "62%", "63%", "64%", "65%", "66%", "67%", "68%", "69%", "70%", "71%", "72%", "73%", "74%", "75%", "76%", "77%", "78%", "79%", "80%", "81%", "82%", "83%", "84%", "85%", "86%", "87%", "88%", "89%", "90%", "91%", "92%", "93%", "94%", "95%", "96%", "97%", "98%", "99%" ]
    if data.message == '':
        data.subClient.send_message(chatId=data.chatId,message=f"{data.author} you are "+str(random.choice(perc))+ " gay")
    else:
        data.subClient.send_message(chatId=data.chatId,message=f"{data.message} is "+str(random.choice(perc))+" gay")
def staff(data):
    return data.subClient.is_in_staff(data.authorId)
@client.command("bio")
def bio(data, condition=staff):
    data.subClient.edit_profile(content=data.message)
    data.subClient.send_message(chatId=data.chatId,message=f"{data.author} has changed my bio to {data.message}")
@client.command("say")
def say(data):
    data.subClient.send_message(chatId=data.chatId,message=data.message)
@client.command("help")
def cjat(data):
    with open("help.png", "rb") as file:
        data.subClient.send_message(data.chatId,file=file, fileType="image")
@client.command("follow_me")
def follow(data):
    usr = data.subClient.get_user_id(data.author)
    print(usr)
    data.subClient.follow_user(usr[1])
    data.subClient.send_message(chatId=data.chatId,message=f"followed,  {data.author}!")
@client.command("bg")
def bg(data):
    image = data.subClient.get_chat_thread(data.chatId).backgroundImage
    if image is not None:
        filename = image.split("/")[-1]
        urllib.request.urlretrieve(image, filename)
        with open(filename, 'rb') as fp:
            data.subClient.send_message(chatId=data.chatId, file=fp, fileType="image")
@client.command("startvc", condition=vip)
def startvc(data):
    client.start_vc(comId=data.comId, chatId=data.chatId)
@client.command("endvc", condition=vip)
def endvc(data):
    client.end_vc(comId=data.comId, chatId=data.chatId)
client.launch(True)
print("Bot is ready")
