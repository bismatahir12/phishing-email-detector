import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
import pickle

# === File paths ===
dataset_path = os.path.join("..", "dataset", "phishing_emails.csv")
model_path = "phishing_model.pkl"
vectorizer_path = "vectorizer.pkl"

# === Load dataset ===
df = pd.read_csv(dataset_path)

# --- Handle column naming flexibility ---
if "email_text" not in df.columns and "text_combined" in df.columns:
    df.rename(columns={"text_combined": "email_text"}, inplace=True)

# Final column check
expected_cols = {"email_text", "label"}
if not expected_cols.issubset(df.columns):
    raise ValueError(f"Dataset must contain columns {expected_cols}, found {list(df.columns)}")

# === Vectorize text ===
vectorizer = TfidfVectorizer(stop_words="english", lowercase=True, max_features=5000)
X = vectorizer.fit_transform(df["email_text"])
y = df["label"]

# Save vectorizer
with open(vectorizer_path, "wb") as f:
    pickle.dump(vectorizer, f)

# === Train-test split ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === Train model ===
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# === Evaluate model ===
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.2%}")

# Save model
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Model saved as {model_path}")
print(f"✅ Vectorizer saved as {vectorizer_path}")
