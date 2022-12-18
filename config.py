import os

BASE_PATH = os.getcwd()

MODEL_PATH = os.path.join(BASE_PATH, r'artifacts/logistic_classifier.pkl')

CSV_PATH = os.path.join(BASE_PATH, r'CSV_Files/cleaned_data.csv')

PORT_NUMBER = 5000