# Flask Webhook for Pharmacy Bot

This file sets up the Flask webhook for handling events.

from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Process the data as needed
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)