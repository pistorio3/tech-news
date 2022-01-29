from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    news_top_five = []
    for element in news:
        element["soma"] = element["shares_count"] + element["comments_count"]
    news.sort(key=lambda element: element["soma"])
    top_five = news[:5]
    for element in top_five:
        news_top_five.append((element["title"], element["url"]))
    return news_top_five


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
