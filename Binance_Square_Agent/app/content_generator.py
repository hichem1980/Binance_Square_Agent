import hashlib
import random
from datetime import datetime, timezone

TOPICS = [
    "Bitcoin",
    "Ethereum",
    "Solana",
    "Stablecoins",
    "DeFi",
    "Layer 2 networks",
    "Crypto regulation",
    "Blockchain security",
    "On-chain analytics",
    "Web3 adoption",
    "Tokenomics",
    "Crypto staking",
    "Institutional crypto adoption",
    "Crypto market sentiment",
]


def generate_title(topic):
    templates = [
        f"{topic}: Key Factors to Watch in the Crypto Market",
        f"Understanding the Role of {topic} in Digital Assets",
        f"{topic}: Opportunities, Risks, and Market Trends",
        f"What Crypto Users Should Know About {topic}",
        f"A Balanced Overview of {topic}",
    ]
    return random.choice(templates)


def article_hash(title, content):
    raw = (title + "\n" + content).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def choose_topic():
    return random.choice(TOPICS)


def generate_article(topic):
    title = generate_title(topic)

    body = f"""\
{title}

The cryptocurrency market is shaped by more than short-term price movements.
Network activity, liquidity, regulation, security, adoption, and real-world
utility all influence how digital assets are perceived by investors and users.

When analyzing {topic}, it is important to separate verified information from
speculation. A project may receive strong attention because of its technology,
ecosystem, or institutional backing, but attention alone does not guarantee
long-term success.

One major factor to consider is practical utility. Projects that solve real
problems and deliver a dependable user experience often build stronger market
foundations than projects driven only by hype. This does not eliminate risk,
because digital assets can still remain highly volatile even when their
technology is promising.

Market participants should also monitor regulatory developments, developer
activity, liquidity, and on-chain metrics. These factors can provide useful
context, but none of them can assure future performance with certainty.

A balanced approach is especially important in crypto markets. Readers should
consult official project documentation, compare multiple reliable sources, and
avoid making decisions based solely on hype, social media activity, or price
momentum.

This article is for educational purposes only and does not constitute
financial, investment, or trading advice.

#{topic.replace(' ', '')} #Crypto #Blockchain #MarketAnalysis
"""

    article = {
        "title": title,
        "content": body.strip(),
        "topic": topic,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "tags": [topic, "Crypto", "Blockchain", "MarketAnalysis"],
    }
    article["hash"] = article_hash(article["title"], article["content"])
    return article
