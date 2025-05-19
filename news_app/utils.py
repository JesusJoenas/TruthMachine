import difflib
import requests
import bleach
from django.conf import settings

# Clean the text by stripping unwanted HTML tags and shorten it if it's too long
def sanitize_and_truncate(text, word_limit=500):
    if not text:
        return ""
    cleaned = bleach.clean(text, tags=['p', 'b', 'i', 'a'], strip=True)
    words = cleaned.split()
    return ' '.join(words[:word_limit]) + '...' if len(words) > word_limit else cleaned

# Check whether an article is very similar to already seen ones (to avoid duplicates)
def is_similar(article, seen_articles, threshold=0.9):
    for seen in seen_articles:
        title_ratio = difflib.SequenceMatcher(None, article['title'], seen['title']).ratio()
        content_ratio = difflib.SequenceMatcher(None, article['content'], seen['content']).ratio()
        if title_ratio > threshold or content_ratio > threshold:
            return True
    return False

# Pull news articles from NewsAPI
def fetch_newsapi(query=None):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        'q': query or '',
        'country': 'us',
        'apiKey': settings.NEWS_API_KEY
    }
    response = requests.get(url, params=params)
    return [{
        'title': a['title'],
        'content': sanitize_and_truncate(a['title'] + ". " + (a.get('description') or '')),
        'url': a['url'],
        'image_url': a.get('urlToImage') or '/static/images/placeholder.jpg'
    } for a in response.json().get('articles', [])]

# Pull articles from The Guardian API
def fetch_guardian(query=None):
    url = "https://content.guardianapis.com/search"
    params = {
        'q': query or '',
        'api-key': settings.GUARDIAN_KEY,
        'show-fields': 'headline,thumbnail,body'
    }
    response = requests.get(url, params=params)
    return [{
        'title': a['webTitle'],
        'content': sanitize_and_truncate(a['webTitle'] + ". " + a['fields'].get('body', '')),
        'url': a['webUrl'],
        'image_url': a['fields'].get('thumbnail') or '/static/images/placeholder.jpg'
    } for a in response.json()['response']['results']]

# # Pull articles from New York Times API
# def fetch_nyt(query=None):
#     url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
#     params = {
#         'q': query or '',
#         'api-key': settings.NYT_KEY
#     }
#     response = requests.get(url, params=params)
#     return [{
#         'title': a['headline']['main'],
#         'content': sanitize_and_truncate(a['headline']['main'] + ". " + (a.get('snippet') or '')),
#         'url': a['web_url'],
#         'image_url': '/static/images/placeholder.jpg'
#     } for a in response.json()['response']['docs']]

# Pull articles from MediaStack API
def fetch_mediastack(query=None):
    url = 'http://api.mediastack.com/v1/news'
    params = {
        'access_key': settings.MEDIASTACK_KEY,
        'keywords': query or '',
        'languages': 'en',
    }
    response = requests.get(url, params=params)
    return [{
        'title': a['title'],
        'content': sanitize_and_truncate(a['title'] + ". " + (a.get('description') or '')),
        'url': a['url'],
        'image_url': a.get('image') or '/static/images/placeholder.jpg'
    } for a in response.json().get('data', [])]

# Pull articles from GNews API
def fetch_gnews(query=None):
    url = 'https://gnews.io/api/v4/search'
    params = {
        'q': query or 'news',
        'token': settings.GNEWS_KEY,
        'lang': 'en',
        'max': 10
    }
    response = requests.get(url, params=params)
    return [{
        'title': a['title'],
        'content': sanitize_and_truncate(a['title'] + ". " + (a.get('description') or '')),
        'url': a['url'],
        'image_url': a.get('image') or '/static/images/placeholder.jpg'
    } for a in response.json().get('articles', [])]

# Combine articles from all sources and remove near-duplicates
def fetch_all_articles(query=None):
    raw_articles = (
        fetch_newsapi(query) +
        fetch_guardian(query) +
        # fetch_nyt(query) +
        fetch_mediastack(query) +
        fetch_gnews(query)
    )

    unique_articles = []
    for article in raw_articles:
        if not is_similar(article, unique_articles):
            unique_articles.append(article)

    return unique_articles
