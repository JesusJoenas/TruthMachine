from django.contrib import admin
from .models import NewsArticle, UserProfile
from .models import Feedback

# Registering the models so they can be managed through the Django admin interface
@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    # Fields to be displayed in the NewsArticle admin list view
    list_display = ['title', 'category', 'publication_date']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Fields to be displayed in the UserProfile admin list view
    list_display = ['user', 'preferred_categories']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    # Fields to be displayed in the Feedback admin list view
    list_display = ['article', 'user', 'rating', 'created_at']
