from asyncio.base_events import Server
import logging
from plugins.telegram_forward_utils.getenv import getenv
from typing import Any, Optional
from mcdreforged.api.command import *
from mcdreforged.api.types import *
from mcdrtelegram import Telegram
import asyncio
from aiogram import types as atypes

# Consts
PLUGIN_METADATA = {
	'id': 'telegram_forward',    # contains letter in lowercase, number and underscore
	'version': '0.1.0',       # recommend to follow semver
	'name': 'Telegram 雙向轉送工具',  # RText component is allowed
	'description': 'Telegram 雙向轉送工具',  # RText component is allowed
	'author': 'pan93412',  # A str, or a list of str
	'link': 'https://github.com/YuutaW-Minecraft/mcdr-telegram',  # A str to your plugin home page
	'dependencies': {
		'mcdreforged': '>=1.0.0',
	}
}
SERVER_SCOPE = "Server"

# Pre-initiation
token = getenv("BOT_TOKEN", "The Telegram bot token.")
chat_id = getenv("BOT_CHATID", "Where to send the messages?")
bot_base = Telegram(token)
bot = bot_base.get_bot()
dp = bot_base.get_dp()
minecraft_server: Optional[ServerInterface] = None

# Library
def send_to_tg(scope: str, message: str):
    asyncio.run(bot.send_message(chat_id, f"<minecraft:{scope}> {message}"))

def send_to_mc(scope: str, message: str):
    minecraft_server.say(f"<telegram:{scope}> {message}")  # type: ignore

# Events from Minecraft
def on_load(server: ServerInterface, old_module: Any):
    global minecraft_server
    minecraft_server = server
    bot_base.start_polling()

def on_unload(server: ServerInterface):
    bot_base.stop_polling()

def on_remove(server: ServerInterface):
    asyncio.run(bot_base.stop_bot())

def on_info(server: ServerInterface, info: Info): pass

def on_user_info(server: ServerInterface, info: Info):
    if info.content:
        send_to_tg(info.player or "?", info.content)

def on_player_joined(server: ServerInterface, player: str, info: Info):
    send_to_tg(SERVER_SCOPE, f"{player} Joined. Welcome!")

def on_player_left(server: ServerInterface, player: str):
    send_to_tg(SERVER_SCOPE, f"{player} Left. See you next time! :)")

def on_server_start(server: ServerInterface): pass

def on_server_startup(server: ServerInterface):
    send_to_tg(SERVER_SCOPE, f"Started. Ready to play!")

def on_server_stop(server: ServerInterface, return_code: int):
    send_to_tg(SERVER_SCOPE, f"Stopping. Game over.")

def on_mcdr_start(server: ServerInterface): pass

def on_mcdr_stop(server: ServerInterface): pass

@dp.message_handler()  # type: ignore
def on_telegram_received_message(message: atypes.Message):
    if minecraft_server == None or message == None:
        logging.warn("minecraft_server or message is none. Ignoring.")
        return

    usr_first_name: str = SERVER_SCOPE if message.from_user == None else message.from_user.first_name
    caption = message.caption if message.caption else ''

    if caption == "#nofwd":
        return

    if message.text not in ['#nofwd', None]:
        text = message.text[:50] + "⋯⋯" if len(message.text) > 50 else message.text
        send_to_mc(usr_first_name, text)
    elif message.sticker != None:
        send_to_mc(usr_first_name, f"(sticker)")
    elif message.photo != None:
        send_to_mc(usr_first_name, "(photo) {caption}")
    elif message.document != None:
        send_to_mc(usr_first_name, "(document) {caption}")
    else:
        send_to_mc(usr_first_name, "There are something new in Telegram!")