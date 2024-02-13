import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "27981265"))
API_HASH = environ.get("API_HASH", "e2e52a1550b8dea246b64617a768eee2")
BOT_TOKEN = environ.get("BOT_TOKEN", "6831175612:AAEO_xY86nFwe-1PZl719vRPnc68RGgFIjs")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "1001923947029"))
ADMINS = int(environ.get("ADMINS", "5236678934"))
DB_URI = environ.get("DB_URI", "mongodb+srv://Akshadgod:14643583pp@cluster0.nnyqicw.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
