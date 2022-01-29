from tech_news.database import find_news
from tech_news.database import db


# Requisito 10
def top_5_news():
    news = find_news()
    news_top_five = []
    for element in news:
        element["soma"] = element["shares_count"] + element["comments_count"]
    # https://docs.python.org/3/howto/sorting.html
    news.sort(key=lambda element: element["soma"], reverse=True)
    top_five = news[:5]
    for element in top_five:
        news_top_five.append((element["title"], element["url"]))
    return news_top_five


# Requisito 11
def top_5_categories():
    categories_top_five = []
    # https://docs.mongodb.com/manual/reference/method/db.collection.aggregate/#examples
    categories_list = db.news.aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
            {"$sort": {"_id": 1}},
        ]
    )
    for category in categories_list:
        categories_top_five.append(category["_id"])
    return categories_top_five[:5]
