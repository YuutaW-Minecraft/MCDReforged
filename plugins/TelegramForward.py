from plugins.telegram_forward_utils.getenv import getenv
from typing import Any
from mcdreforged.api.command import *
from mcdreforged.api.types import *
from mcdrtelegram import Telegram

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

# Library
def send_to_tg(scope: str, message: str):
    return bot.send_message(chat_id, f"{scope}: {message}")

# Events from Minecraft
def on_load(server: ServerInterface, old_module: Any):
    return bot_base.start_polling()

def on_unload(server: ServerInterface):
    bot_base.stop_polling()

def on_remove(server: ServerInterface):
    return bot_base.stop_bot()

def on_info(server: ServerInterface, info: Info):
    if info.content:
        return send_to_tg(SERVER_SCOPE, info.content)
    return None

def on_user_info(server: ServerInterface, info: Info):
    if info.content:
        return send_to_tg(info.player or "?", info.content)
    return None

def on_player_joined(server: ServerInterface, player: str, info: Info):
    return send_to_tg(SERVER_SCOPE, f"{player} Joined. Welcome!")

def on_player_left(server: ServerInterface, player: str):
    return send_to_tg(SERVER_SCOPE, f"{player} Left. See you next time! :)")

def on_server_start(server: ServerInterface): pass

def on_server_startup(server: ServerInterface):
    return send_to_tg(SERVER_SCOPE, f"Started. Ready to play!")

def on_server_stop(server: ServerInterface, return_code: int):
    return send_to_tg(SERVER_SCOPE, f"Stopping. Game over.")

def on_mcdr_start(server: ServerInterface): pass

def on_mcdr_stop(server: ServerInterface): pass
