from tech_news.database import db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    search = db.news.find({
        "title": {
            "$regex": title,
            "$options": "i"
        }
    })
    list_news = []
    for element in search:
        list_news.append((
            element["title"],
            element["url"]
        ))
    return list_news


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    search = db.news.find({
        "timestamp": {
            "$regex": date
        }
    })
    list_news = []
    for element in search:
        list_news.append((
            element["title"], element["url"]
        ))
    return list_news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
