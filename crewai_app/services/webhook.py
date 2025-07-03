# Optional Flask server for webhooks
from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Handle webhook event
    return {'status': 'received'}
