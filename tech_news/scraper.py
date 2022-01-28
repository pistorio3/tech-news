import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("div.tec--card__info > h3 > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".tec--btn--lg::attr(href)").get()


# Função auxiliar req4
def get_writer(selector):
    try:
        writer = selector.css(".z--font-bold *::text").get().strip()
        return writer
    except AttributeError:
        return None


# Função auxiliar req4
def get_shares(selector):
    try:
        shares_count = (
            selector.css('.tec--toolbar__item::text').get().strip()
        )
        return int(shares_count[0])
    except AttributeError:
        return 0


# Função auxiliar req4
def get_comments(selector):
    comments_count = selector.css('#js-comments-btn::attr(data-count)').get()
    return int(comments_count)


# Função auxiliar req4
def get_sources(selector):
    sources = selector.css('.z--mb-16 .tec--badge::text').getall()
    return [source.strip() for source in sources]


# Função auxiliar req4
def get_categories(selector):
    categories = selector.css('#js-categories > a::text').getall()
    return [category.strip() for category in categories]


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    date = selector.css("#js-article-date::attr(datetime)").get()
    summary = "".join(
        selector.css(
            ".tec--article__body > p:nth-child(1) ::text"
        ).getall()
    )
    return {
        "url": url,
        "title": title,
        "timestamp": date,
        "writer": get_writer(selector),
        "shares_count": get_shares(selector),
        "comments_count": get_comments(selector),
        "summary": summary,
        "sources": get_sources(selector),
        "categories": get_categories(selector),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
