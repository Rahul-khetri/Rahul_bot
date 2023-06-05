from telethon import events
from .. import bot
from .. import openai_key
import asyncio
import openai

openai_key ="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"
openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True, pattern= "(?!)/ask"))
async def chatgpt(event):
  if event.sender_id == int() :
    await event.reply(f"{events}")