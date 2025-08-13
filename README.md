Phishing Email Detector
=======================

This project is a Machine Learning-based web application that detects whether a given email text is **phishing** or **Not phishing**.  
It uses a trained classification model along with a text vectorizer to analyze the email content and predict its category.

##  Live Application
Deployed App: [https://phishing-email-detector-silk.vercel.app/](https://phishing-email-detector-silk.vercel.app/)

------------------------------------------------
 Features
------------------------------------------------
- **Email Text Classification** – Detects phishing vs. legitimate emails.
- **Machine Learning Model** – Trained using scikit-learn.
- **Flask Web App** – Simple and interactive web interface.
- **Vectorizer Integration** – Transforms text input into numerical features for the model.
- **API Support** – Can be tested via Postman or curl commands.


------------------------------------------------
⚙️ Installation & Setup
------------------------------------------------
1. **Clone the repository**
git clone https://github.com/bismatahir12/phishing-email-detector.git
cd phishing-email-detector


2. **Create a virtual environment (optional but recommended)**
python -m venv venv
source venv/bin/activate # For Linux/Mac
venv\Scripts\activate # For Windows


3. **Install dependencies**
pip install -r requirements.txt


4. **Train the model (optional if model.pkl is already provided)**
python model/train_model.py


5. **Run the application**
python app.py


6. **Access the app**
- Open your browser and go to: `http://127.0.0.1:5000`

------------------------------------------------
 Testing via Postman or curl
------------------------------------------------
You can send a POST request to test the API endpoint:

**POST** `http://127.0.0.1:5000/predict`

**Body (JSON):**
{
"email_text": "Congratulations! You've won a lottery. Click here to claim your prize."
}

**Response:**
{
"prediction": "Phishing"
}

------------------------------------------------
 Model Details
------------------------------------------------
- **Algorithm:** Logistic Regression (can be replaced with other classifiers)
- **Dataset:** Labeled phishing & legitimate email dataset
- **Text Preprocessing:** Tokenization, lowercasing, stopword removal, vectorization using `TfidfVectorizer`

------------------------------------------------
 Future Improvements
------------------------------------------------
- Add URL analysis for phishing detection
- Use deep learning models (e.g., LSTM, BERT)
- Integrate with email APIs for real-time detection
- Improve UI with Bootstrap





