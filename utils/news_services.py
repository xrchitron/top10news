import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from the .env file

from newsapi import NewsApiClient
news_api = NewsApiClient(api_key=os.environ.get('NEWS_SECRET_KEY'))


def news_from_news_api():
    news_sources = ['bbc-news', 'cnn', 'google-news']
    news_pool = []
    for news_author in news_sources:
        # url = f"https://newsapi.org/v2/top-headlines?sources={news_author}&apiKey={os.environ.get('NEWS_SECRET_KEY')}"
        # news = requests.get(url)
        news = news_api.get_top_headlines(sources=news_author, page_size=10)
        articles = news['articles']
        news_pool.append(articles)

    return news_pool