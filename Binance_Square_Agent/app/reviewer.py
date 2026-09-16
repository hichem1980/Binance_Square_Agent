def review_article(article):
    title = article["title"].strip()
    content = article["content"].strip()
    issues = []

    if len(title) < 12:
        issues.append("Title is too short")
    if len(content) < 300:
        issues.append("Content is too short")
    if "guaranteed profit" in content.lower():
        issues.append("Contains risky profit claim")
    if "buy now" in content.lower():
        issues.append("Contains promotional language")

    return {
        "approved": len(issues) == 0,
        "issues": issues,
    }
