from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Handle incoming messages from Twilio
    data = request.json
    print(data)  # Log incoming data for debugging
    # Add your logic to handle the incoming message here
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)