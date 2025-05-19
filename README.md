# TruthMachine

TruthMachine is a Django-based web application designed to personalize and evaluate news articles using machine learning. Unlike typical news aggregators, this platform not only recommends articles based on user preferences but also performs fact-checking to determine how credible each article is.

The core feature of TruthMachine is a custom-trained logistic regression model that analyzes article content and assigns a truth score. This score reflects the likelihood that the article is factually accurate, helping users critically assess what they read. The model is trained on labeled datasets of real and fake news articles, using TF-IDF vectorization and a supervised learning approach.

The system also includes user registration, login, article search, a personalized dashboard, and a feedback form for continual improvement.

## Features

- Truth score generation using a logistic regression fact-checking model
- User authentication (registration, login, logout, password reset)
- Search interface for querying news articles in real time
- Personalized dashboard based on user interest
- Article detail view with credibility score
- Feedback form to enhance recommendation quality
- Admin panel for managing users and content

## Technologies Used

- Django (Python Web Framework)
- SQLite (Development database)
- HTML, CSS, Bootstrap (Frontend UI)
- TF-IDF & Logistic Regression (Machine Learning for fact checking)
- News APIs (e.g., New York Times API, GNews)
- Matplotlib (for visualizing ROC curve)
- Joblib (for saving trained model and vectorizer)

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/JesusJoenas/TruthMachine.git
   cd TruthMachine
   ```

2. **Create and activate a virtual environment**

   On Windows:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations and start the server**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the app**

   Navigate to: `http://127.0.0.1:8000/`

## Admin Access

Create a superuser account:

```bash
python manage.py createsuperuser
```

Then log in at `http://127.0.0.1:8000/admin/`

## Project Structure

- `manage.py` – Entry point for Django commands
- `personalised_news/` – Main project settings
- `news_app/` – Application logic (models, views, URLs, utils)
- `templates/` – HTML templates for frontend rendering
- `static/` – CSS, JavaScript, and image assets
- `fact_check_model/` – Contains trained model, vectorizer, and ROC curve
- `requirements.txt` – Python dependencies

## Author

Developed by Jesus Joenas as part of a software engineering project exploring personalized content delivery and automated fact-checking.

GitHub: [https://github.com/JesusJoenas](https://github.com/JesusJoenas)  
Portfolio: [https://jesusjoenas.github.io](https://jesusjoenas.github.io)
