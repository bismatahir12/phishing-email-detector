"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import ai_phishing_email_detector.app
