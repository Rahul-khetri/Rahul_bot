from telethon import TelegramClient
import logging
import time
openai_key ="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"

api_id ="1125689"
api_hash ="4772d1792ed194020a8fb06a91ffb8fa"

bot_token ="5851167169:AAHme1gljkjYn6jTw-y3xaXoUIw5blyIR0g"

bot =  TelegramClient("projectbot", api_id, api_hash).start(bot_token=bot_token)
