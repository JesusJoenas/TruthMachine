# TruthMachine

TruthMachine is a web-based application built with Django that delivers personalized news articles to users using machine learning. The aim of this project is to explore how recommendation systems can enhance user experience by tailoring news content based on individual preferences and search activity.

The system connects to news APIs, filters articles based on user input, and presents them in a structured and accessible format. It also allows for user registration, secure login, article searching, and feedback submission to continuously refine recommendations.

## Features

- User authentication (register, login, logout)
- Password reset via email
- Search interface for querying current news
- Personalized dashboard with article recommendations
- Article detail view for reading selected articles
- Feedback form for improving recommendation logic
- Admin access for managing users and content

## Technologies Used

- Django (Python Web Framework)
- SQLite (Default database for development)
- HTML, CSS, Bootstrap (Frontend styling)
- News APIs (e.g., New York Times API)
- Machine learning (basic recommendation logic)
- Optional: Firebase for extended functionality

## Getting Started

To run the project locally:

1. **Clone the repository**

   ```
   git clone https://github.com/JesusJoenas/TruthMachine.git
   cd TruthMachine
   ```

2. **Create and activate a virtual environment**

   On Windows:

   ```
   python -m venv myenv
   myenv\Scripts\activate
   ```

   On macOS/Linux:

   ```
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install the required packages**

   ```
   pip install -r requirements.txt
   ```

4. **Apply migrations and start the server**

   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the application**

   Open your browser and go to `http://127.0.0.1:8000/`

## Admin Access

To access the admin panel, create a superuser:

```
python manage.py createsuperuser
```

Then navigate to `http://127.0.0.1:8000/admin/` and log in with your credentials.

## Project Structure

- `manage.py` – Entry point for Django commands
- `personalised_news/` – Project settings and configuration
- `news_app/` – Main application containing views, URLs, and logic
- `templates/` – HTML files for rendering frontend
- `static/` – Static assets such as CSS and JS files
- `requirements.txt` – List of dependencies

## Author

This project was developed by Jesus Joenas as part of a software engineering assignment to demonstrate full-stack development skills using Django and machine learning concepts.

GitHub: [https://github.com/JesusJoenas](https://github.com/JesusJoenas)  
Portfolio: [https://jesusjoenas.github.io](https://jesusjoenas.github.io)
