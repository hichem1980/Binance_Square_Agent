from app.config import REQUIRE_HUMAN_APPROVAL
from app.content_generator import choose_topic, generate_article
from app.database import article_exists, increment_today_success_count, init_db, save_log, save_post
from app.limiter import can_publish_today
from app.reviewer import review_article
from app.binance_square_client import publish_to_binance_square


def process_one_article():
    if not can_publish_today():
        msg = "Daily post limit reached: 99 successful posts."
        save_log({"event": "limit_reached", "message": msg})
        print(msg)
        return False

    topic = choose_topic()
    article = generate_article(topic)

    if article_exists(article["hash"]):
        save_log({"event": "duplicate", "topic": topic, "title": article["title"]})
        print("Duplicate article detected. Skip.")
        return False

    review = review_article(article)
    if not review["approved"]:
        msg = f"Rejected by reviewer: {review['issues']}"
        save_log({"event": "review_failed", "topic": topic, "issues": review["issues"]})
        print(msg)
        return False

    if REQUIRE_HUMAN_APPROVAL:
        save_log({"event": "waiting_approval", "topic": topic})
        print("Human approval required before publishing.")
        return False

    result = publish_to_binance_square(article)

    if result["status"] == "success":
        save_post(
            title=article["title"],
            topic=article["topic"],
            content=article["content"],
            status="success",
            platform="binance_square",
            article_hash=article["hash"],
        )
        increment_today_success_count()
        save_log({"event": "published", "title": article["title"], "topic": article["topic"]})
        print(f"Published: {article['title']}")
        return True

    save_post(
        title=article["title"],
        topic=article["topic"],
        content=article["content"],
        status="error",
        platform="binance_square",
        article_hash=article["hash"],
    )
    save_log({"event": "publish_failed", "title": article["title"], "details": result})
    print(result)
    return False


if __name__ == "__main__":
    init_db()
    process_one_article()
