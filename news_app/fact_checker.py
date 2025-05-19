import joblib
import os
import re
import string

# Set up the base directory to locate the model and vectorizer files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define paths for the saved model and vectorizer
model_path = os.path.join(BASE_DIR, 'news_app', 'fact_check_model', 'fact_checker_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'news_app', 'fact_check_model', 'fact_checker_vectorizer.pkl')

# Load the trained Logistic Regression model and TF-IDF vectorizer
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Helper function to clean and preprocess the input text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)  # Remove text in brackets
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove URLs
    text = re.sub(r'<.*?>+', '', text)  # Remove HTML tags
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # Remove punctuation
    text = re.sub(r'\n', '', text)  # Remove newlines
    text = re.sub(r'\w*\d\w*', '', text)  # Remove words containing numbers
    return text

# Main function to predict the truth probability of an article
def fact_check_article(text):
    if not text:
        return 0  # Return 0% true if no content is provided (edge case handling)

    cleaned_text = clean_text(text)
    features = vectorizer.transform([cleaned_text])
    probability_true = model.predict_proba(features)[0][1]  # Extract probability that article is true
    return round(probability_true * 100, 2)  # Convert to percentage format
