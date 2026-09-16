import requests

from app.config import BINANCE_SQUARE_API_KEY, BINANCE_SQUARE_POST_URL


def publish_to_binance_square(article):
    if not BINANCE_SQUARE_API_KEY:
        raise ValueError("BINANCE_SQUARE_API_KEY is missing.")

    if not BINANCE_SQUARE_POST_URL or "example" in BINANCE_SQUARE_POST_URL:
        raise ValueError(
            "BINANCE_SQUARE_POST_URL is not configured. Update it with the official Binance Square posting endpoint."
        )

    payload = {
        "title": article["title"],
        "content": article["content"],
        "tags": article.get("tags", []),
        "topic": article.get("topic", ""),
    }

    headers = {
        "Authorization": f"Bearer {BINANCE_SQUARE_API_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(BINANCE_SQUARE_POST_URL, headers=headers, json=payload, timeout=30)

    try:
        response.raise_for_status()
        return {
            "status": "success",
            "http_status": response.status_code,
            "body": response.json(),
        }
    except requests.HTTPError:
        return {
            "status": "error",
            "http_status": response.status_code,
            "body": response.text,
        }
