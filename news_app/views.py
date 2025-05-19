from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import NewsArticle, UserProfile, Feedback
from .utils import fetch_all_articles
from .recommender import recommend_news
from .forms import FeedbackForm
from .fact_checker import fact_check_article

def home(request):
    # Handle the homepage and search for articles if a query is given
    query = request.GET.get('q')
    articles = fetch_all_articles(query)
    return render(request, 'news_app/home.html', {'articles': articles})

@login_required
def landing_page(request):
    # After login, land users here
    return render(request, 'news_app/landing.html')

@login_required
def dashboard(request):
    # Load dashboard with recommended articles for logged-in users
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    articles = get_recommended_articles(user_profile)
    return render(request, 'news_app/dashboard.html', {'articles': articles})

def search_news(request):
    # Handle the search functionality
    query = request.GET.get('q')
    articles = []

    if query:
        articles = fetch_all_articles(query)
    else:
        query = ""

    return render(request, 'news_app/search.html', {'articles': articles, 'query': query})

def get_recommended_articles(user_profile):
    # Just mocking some recommended articles for now
    return [
        {
            'title': 'Tech Update: AI is Taking Over!',
            'content': 'AI is making waves in every sector...',
            'url': 'https://example.com/ai-news',
            'image_url': 'https://via.placeholder.com/300'
        },
        {
            'title': 'World News: Market Hits Record High',
            'content': 'The stock market reached new heights...',
            'url': 'https://example.com/market-news',
            'image_url': 'https://via.placeholder.com/300'
        },
    ]

def login_view(request):
    # Manage user login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('landing_page')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')

    return render(request, 'news_app/login.html')

def logout_view(request):
    # Log the user out
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

def register(request):
    # Handle user registration
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        # Check if email is already taken
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        # Create and save the new user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )

        user.save()
        messages.success(request, "Account successfully created! You can now log in.")
        return redirect('login')

    return render(request, 'news_app/register.html')

def article_detail(request):
    # Display the detailed view for a specific article
    title = request.GET.get('title')
    content = request.GET.get('content')
    article_url = request.GET.get('url')
    query = request.GET.get('q')

    # Run fact-checking analysis
    truth_score = fact_check_article(content) if content else None

    context = {
        'title': title,
        'content': content,
        'article_url': article_url,
        'truth_score': truth_score,
        'query': query,
    }

    return render(request, 'news_app/article_detail.html', context)

def feedback(request):
    # Handle feedback form submission
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('home')
    else:
        form = FeedbackForm()
        
    return render(request, 'news_app/feedback.html', {'form': form})
