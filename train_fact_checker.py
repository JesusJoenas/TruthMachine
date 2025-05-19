import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import joblib
import os

# Load the datasets containing fake and true news articles
fake = pd.read_csv('C:/datasets/Fake.csv')
true = pd.read_csv('C:/datasets/True.csv')

# Assign labels manually: 0 for Fake news, 1 for Real news
fake['label'] = 0
true['label'] = 1

# Merge the two datasets into a single dataframe
data = pd.concat([fake, true])

# Randomly shuffle the dataset to prevent ordering bias
data = data.sample(frac=1).reset_index(drop=True)

# Focus only on the article text and its corresponding label
X = data['text']
y = data['label']

# Split the data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Transform the text data into numerical format using TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# Initialize and train the Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vectors, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_vectors)
y_pred_proba = model.predict_proba(X_test_vectors)[:, 1]

# Evaluate the model’s performance using several important metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba)

# Print out the evaluation results nicely formatted
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall: {recall * 100:.2f}%")
print(f"F1 Score: {f1 * 100:.2f}%")
print(f"AUC Score: {auc:.4f}")

# Generate the confusion matrix to get a better breakdown of correct vs incorrect classifications
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Plot the ROC Curve for a visual representation of performance
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {auc:.3f})')
plt.plot([0,1], [0,1], linestyle='--', color='gray')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for Fake News Detection')
plt.legend(loc='lower right')
plt.grid()
plt.tight_layout()

# Save the ROC Curve figure into the appropriate folder
os.makedirs('news_app/fact_check_model', exist_ok=True)
plt.savefig('news_app/fact_check_model/roc_curve.png')

print("\nROC Curve saved as 'roc_curve.png' inside 'news_app/fact_check_model/'.")

# Finally, save both the trained model and the TF-IDF vectorizer for later use
joblib.dump(model, 'news_app/fact_check_model/fact_checker_model.pkl')
joblib.dump(vectorizer, 'news_app/fact_check_model/fact_checker_vectorizer.pkl')

print("Model and vectorizer saved successfully!")
