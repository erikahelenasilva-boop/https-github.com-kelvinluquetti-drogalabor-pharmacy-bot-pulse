# WhatsApp Pharmacy Bot Documentation

## Overview
This project is a WhatsApp pharmacy bot that utilizes Twilio's API to provide pharmacy-related services through WhatsApp. The bot can answer queries, handle prescriptions, and provide information about medications.

## Features
- Query handling for medications and prescriptions.
- User-friendly interaction via WhatsApp.
- Integration with Twilio for messaging.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- A Twilio account.
- Node.js installed on your machine.
- Basic understanding of JavaScript.

## Installation
To install the bot, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/kelvinluquetti/drogalabor-pharmacy-bot-pulse.git
   ```
2. Navigate into the project directory:
   ```bash
   cd drogalabor-pharmacy-bot-pulse
   ```
3. Install the required dependencies:
   ```bash
   npm install
   ```

## Configuration
1. Obtain your Twilio credentials from the Twilio console.
2. Create a `.env` file in the root directory of the project, and add the following:
   ```env
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   ```
3. Ensure that your WhatsApp sandbox is set up in Twilio.

## Deployment
You can deploy the bot to any server that supports Node.js. Here are general deployment instructions:
1. Choose a cloud provider (e.g., Heroku, AWS, DigitalOcean).
2. Follow their specific instructions for deploying Node.js applications.
3. Ensure environmental variables are set correctly on the server.

## Usage
- Start the bot:
  ```bash
  node index.js
  ```
- Interact with the bot through WhatsApp by sending messages to the Twilio number.

## Contributing
If you want to contribute to the project, feel free to submit a Pull Request. You can also report issues or suggest features.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.