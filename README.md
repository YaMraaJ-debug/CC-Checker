
This is a Telegram bot written in Python using the Pyrogram framework. The bot fetches card information from a specific Telegram channel and performs actions based on the fetched data.

## Prerequisites

Before running the bot, make sure you have the following prerequisites installed:

- Python 3.8 or higher
- pip package manager

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BalaPriyan/CC-Checker.git

1. Change into the project directory:
   cd telegram-bot


2. Install the required packages:
   pip install -r requirements.txt

## Configuration



1.Open the config.py file in a text editor.

2.Replace the following placeholders with your own values:

API_ID: Your Telegram API ID obtained from the Telegram API platform.
API_HASH: Your Telegram API hash obtained from the Telegram API platform.
PHONE_NUMBER: Your phone number associated with your Telegram account.
CHANNEL: The channel URL or username where you want to fetch the messages from.
LOG_CHANNEL: The username or ID of your log channel where the mirrored activities will be sent.
BOT_USERNAME: Your bot's username.
MONGO_URI: Your MongoDB connection URI.
DATABASE_NAME: The name of the MongoDB database to use.
COLLECTION_NAME: The name of the MongoDB collection to use.
TELEGRAPH_TOKEN: Your Telegraph token obtained from the Telegraph API platform.


## Usage



1.Run the bot using the following command:

   python bot.py

2.The bot will connect to the specified Telegram channel, fetch card information, and perform actions based on the fetched data.

3.The bot will also send a welcome message with a button to the log channel and the user. The user can click the button to access the bot.

## Contributing


Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License


This project is licensed under the MIT License.


You can create a `README.md` file in your project's root directory and replace the placeholders with the appropriate information for your bot. This `README.md` file provides instructions on installation, configuration, usage, and contributing to the project. Additionally, it includes a license section where you can specify the license for your bot (e.g., MIT License). Feel free to customize the file according to your needs and add any additional sections or information as required.
