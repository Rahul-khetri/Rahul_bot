from telethon import TelegramClient
import logging
import time


api_id ="1125689"
api_hash ="4772d1792ed194020a8fb06a91ffb8fa"

bot_token ="5851167169:AAFygiTtSBJ9mU4HbZNkdcNq1O0INAbJaEg"

bot =  TelegramClient("projectbot", api_id, api_hash).start(bot_token=bot_token)
