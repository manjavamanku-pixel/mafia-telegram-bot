import os

BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")
OWNER_ID: int = int(os.environ.get("OWNER_ID", "0"))
DATABASE_URL: str = os.environ.get("DATABASE_URL", "")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN muhit o'zgaruvchisi o'rnatilmagan!")
if not OWNER_ID:
    raise ValueError("OWNER_ID muhit o'zgaruvchisi o'rnatilmagan!")
