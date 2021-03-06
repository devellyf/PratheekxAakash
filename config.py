import os
from os import getenv

from dotenv import load_dotenv

from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Aturma_Vcbot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/20147c4f049e2c1f2f248.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/5e44e711102d74c05314d.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/73e10ed6e2bd32b478de6.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/87e5179763bcf8b88a14b.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a52420989a2265617986a.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "SHIZUKA_ASSISTANT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PratheekXD")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "SHIZUKA_VC_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ABOUTPRATHEEK")
# Fill with your username without a symbol @
OWNER_NAME = getenv("OWNER_NAME", "Pratheek06")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "Pratheek")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/PratheekXD/PratheekxAakash"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
