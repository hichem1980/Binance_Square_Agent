import json
import os
import sqlite3
from datetime import date, datetime

from app.config import DB_PATH, LOG_PATH


def ensure_dirs():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)


def init_db():
    ensure_dirs()
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT,
            title TEXT,
            topic TEXT,
            status TEXT,
            platform TEXT,
            content TEXT,
            article_hash TEXT UNIQUE
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS daily_stats (
            day TEXT PRIMARY KEY,
            successful_posts INTEGER DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


def article_exists(article_hash):
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT 1 FROM posts WHERE article_hash = ?",
        (article_hash,),
    ).fetchone()
    conn.close()
    return row is not None


def save_post(title, topic, content, status, platform, article_hash):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        INSERT INTO posts (created_at, title, topic, status, platform, content, article_hash)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            datetime.utcnow().isoformat(),
            title,
            topic,
            status,
            platform,
            content,
            article_hash,
        ),
    )
    conn.commit()
    conn.close()


def get_today_success_count():
    today = str(date.today())
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT successful_posts FROM daily_stats WHERE day = ?",
        (today,),
    ).fetchone()
    conn.close()
    return int(row[0]) if row else 0


def increment_today_success_count():
    today = str(date.today())
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT successful_posts FROM daily_stats WHERE day = ?",
        (today,),
    ).fetchone()
    if row:
        conn.execute(
            "UPDATE daily_stats SET successful_posts = successful_posts + 1 WHERE day = ?",
            (today,),
        )
    else:
        conn.execute(
            "INSERT INTO daily_stats (day, successful_posts) VALUES (?, 1)",
            (today,),
        )
    conn.commit()
    conn.close()


def save_log(entry):
    ensure_dirs()
    try:
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        data = []

    data.append(entry)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
