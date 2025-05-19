from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Main homepage
    path('', views.home, name='home'),

    # User authentication routes
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # User landing page after login
    path('landing/', views.landing_page, name='landing_page'),

    # Search page where users can find news articles
    path('search/', views.search_news, name='search_news'),

    # Personalized user dashboard with recommended articles
    path('dashboard/', views.dashboard, name='dashboard'),

    # Detailed view of a single article
    path('article_detail/', views.article_detail, name='article_detail'),

    # Feedback form for user input
    path('feedback/', views.feedback, name='feedback'),

    # Password Reset Workflows (built-in Django auth views)
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='news_app/password_reset_form.html'
         ),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='news_app/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='news_app/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='news_app/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
