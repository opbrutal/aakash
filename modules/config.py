# ๐๐จ๐๐ฎ๐ฅ๐๐ฌ ๐๐ง๐ ๐๐ง๐ฏ๐ข๐ซ๐จ๐ง๐ฆ๐๐ง๐ญ๐ฌ
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# ๐๐ง๐ญ๐๐ซ๐ง๐๐ฅ ๐๐๐ซ๐ข๐๐๐ฅ๐๐ฌ (@๐๐๐ข๐ญ๐ฒ๐๐๐๐ฅ๐๐๐ซ)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# ๐๐๐ช๐ฎ๐ข๐ซ๐๐ ๐๐๐ซ๐ข๐๐๐ฅ๐๐ฌ //๐๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ @๐๐๐ข๐ญ๐ฒ๐๐๐๐ฅ๐๐๐ซ
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXXXX")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/55a3552a9184f40a891c0.jpg")
BOT_NAME = getenv("BOT_NAME", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "เผเคฎเฅ๐๐๐ผ๐ใOWNER")
OWNER_USERNAME = getenv("OWNER_USERNAME", "OFFICIAL_MENTALMOD")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/opbrutal/tgmusicbot")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2035495883").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/S4SAHILHACKER")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/ABOUT_BRUTU_DISCUSSION_GROUP")

# ๐๐จ ๐๐จ๐ญ ๐๐ก๐๐ง๐ ๐ ๐๐ก๐ข๐ฌ ๐๐ข๐ง๐๐ฌ // ๐๐ ๐ง๐จ๐ซ๐ ๐๐ก๐ข๐ฌ (เผเคฎเฅ๐๐๐ผ๐ใOWNER ) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/MENTAL_MOD")
