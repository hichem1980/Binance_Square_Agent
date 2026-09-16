from app.config import MAX_POSTS_PER_DAY
from app.database import get_today_success_count


def can_publish_today():
    return get_today_success_count() < MAX_POSTS_PER_DAY
