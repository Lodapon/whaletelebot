
# coding: utf-8

# # Telegram Bot for Whaleoffspring

# In[ ]:


import telebot
import time
from PIL import Image
import requests
from io import BytesIO
import os


# In[ ]:


TOKEN = "1608557385:AAH_YHxWOGr2Wd2TSk8nO-oc6wdpOZ3Gezo"

bot = telebot.TeleBot(TOKEN)


# In[ ]:


@bot.message_handler(commands=["start"])
def start(message):
    print(message.text)
    
#These for bot to reply to specific command with /
@bot.message_handler(commands=["hello","hi"])
def hello(message):
    bot.send_message(message.chat.id, "Hello there!")
    
@bot.message_handler(commands=["contract","Contract"])
def contract(message):
    bot.send_message(message.chat.id, "0x6402af56201e2ba8dc6642750b0a3775d2104d14")
    
@bot.message_handler(commands=["graph","Graph","chart","Chart"])
def graph(message):
    bot.send_message(message.chat.id, "https://poocoin.app/tokens/0x6402af56201e2ba8dc6642750b0a3775d2104d14")
    
@bot.message_handler(commands=["web","site","Web","Site","Website"])
def website(message):
    bot.send_message(message.chat.id, "https://whaleoffspring.com/")
    
# To send an Image
airdrop1stIMGlink = "https://whaleoffspring.com/images/airdropprize_1st.png"
@bot.message_handler(commands=["lotto","Lotto","airdrop","Airdrop","Promotion","promotion"])
def lotto(message):
    response = requests.get(airdrop1stIMGlink)
    imgnet = Image.open(BytesIO(response.content))
    #Send the photo
    bot.send_photo(message.chat.id, imgnet)
    
# To send Video
vdourl = "https://whaleoffspring.com/images/underwater30.mp4"
def dl_file(url, name="video.mp4"):
    r = requests.get(url, stream=True)
    with open(name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
@bot.message_handler(commands=["vdo","bg","underwater"])
def vdonet(message):
    dl_file(vdourl, "bg.mp4")
    vidnet = open("bg.mp4","rb")
    bot.send_video(message.chat.id, vidnet)
                            
# To send sticker
@bot.message_handler(commands=["hold","hodl"])
def hodl(message):
    bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAECUg1gpjB126eFHXWjwQ3h8FZ8u29O2QACygIAA_uYVNz9lXeiMVtgHwQ")
@bot.message_handler(commands=["moon","Moon","tothemoon"])
def moon(message):
    bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAECUg9gpjh15CeYVw2InsN1oHr3481FewACEwMAAjikmVS8RTebivEAAbIfBA")
@bot.message_handler(commands=["lambo","sport"])
def lambo(message):
    bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAECUhFgpjjN7SfihfpVDQcfXFrsTVq4vAACiwQAApJ-mFRmIH9Y6TpRlR8E")

while True:
    try:
        bot.polling()
    except:
        time.sleep(5)

