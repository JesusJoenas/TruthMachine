import random
from .models import NewsArticle

def recommend_news(user_profile):
    preferred_categories = user_profile.preferred_categories.split(",")
    recommended_articles = NewsArticle.objects.filter(category__in=preferred_categories)
    
    if not recommended_articles:
        recommended_articles = NewsArticle.objects.all()[:10]  # Fallback to general articles
    
    return random.sample(list(recommended_articles), min(5, len(recommended_articles)))