from telethon import events
from .. import bot
from .. import openai_key
import asyncio
import openai
from telethon.tl.custom import Button
openai_key ="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"
openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True, pattern="(?i)/ask"))
async def chatgpt(event):
  sender_id = event.sender_id
    await event.reply(f"{event}")
    rahul_msg =("Hello this is Rahul that can talk to anyone")
    await bot.send_msg(sender_id. rahul_msg)