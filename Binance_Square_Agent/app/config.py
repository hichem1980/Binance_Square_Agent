import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

BINANCE_SQUARE_API_KEY = os.getenv("BINANCE_SQUARE_API_KEY", "")
BINANCE_SQUARE_POST_URL = os.getenv("BINANCE_SQUARE_POST_URL", "")
MAX_POSTS_PER_DAY = int(os.getenv("MAX_POSTS_PER_DAY", "99"))
POST_INTERVAL_MINUTES = int(os.getenv("POST_INTERVAL_MINUTES", "180"))
REQUIRE_HUMAN_APPROVAL = os.getenv("REQUIRE_HUMAN_APPROVAL", "false").lower() == "true"

DB_PATH = os.path.join(DATA_DIR, "posts.db")
LOG_PATH = os.path.join(DATA_DIR, "posts.json")
