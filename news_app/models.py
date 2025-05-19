from django.db import models
from django.contrib.auth.models import User

# Define the database models here
class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=100)
    url = models.URLField(max_length=300, blank=True)
    image_url = models.URLField(max_length=300, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_categories = models.CharField(max_length=255)
    viewed_articles = models.ManyToManyField(NewsArticle, blank=True)

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, 'Dislike'), (2, 'Neutral'), (3, 'Like')])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.article.title}'
