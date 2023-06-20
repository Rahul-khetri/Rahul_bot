from .. import bot
from telethon import events
import asyncio




@bot.on(events.NewMessage(incoming=True,pattern="/start"))
async def start(event):
  await event.reply("Hello! This is gabbar_is_back_Bot \n\nType **/help** for the further information")
  
  
@bot.on(events.NewMessage(incoming=True , pattern="/get"))
async def start(event):
  await event.reply("Hello This is get command")
async def start(event):
  a = await event.reply("Hello! Tis is get command")
  await asyncio.sleep(1)
  await a.edit("This is edited message")
  
@bot.on(events.NewMessage(incoming=True, pattern="/eval"))
async def start(event):
  await event.reply("Hello! This is eval command")
@bot.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
  await event.reply("Hello Sir/Ma'am😊 I hope you are good and having a great day. I am gabbar_is_back_Bot developed by RAHUL SAINI. Here are my following command :- \n\n1. /yta + 'link of any YouTube video' = It can help you to download the audio from YouTube Platform.\n\n2. /ytv + 'link of any YouTube video' = It can help you to download the video from YouTube Platform.\n\n3. /tr + 'language code' + 'any sentence as well as emoji' = It can translate the sentence into the language code you have entered.\n\n4. /joke ='It will provide you randomly a joke that i m written in the list'.""
  )
