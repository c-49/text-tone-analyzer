from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

sentiment_model = pipeline("sentiment-analysis")

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    if data and 'text' in data:
        text = data['text']
        result = sentiment_model(text)
        response = make_response(jsonify(result))
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        return response
    else:
        return make_response(jsonify({"error": "Invalid input"}), 400)

if __name__ == '__main__':
    app.run(debug=True)
