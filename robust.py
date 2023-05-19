
import re
import os
import json
import time
import requests
import sqlite3
from urllib.parse import urlparse, urlunparse
import urllib.request
import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_KEY')

# Define a regular expression pattern to match URLs
url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

yellow = '\033[33m'
blue = '\033[34m'
reset = '\033[0m'
pikachu = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢿⡟⠀⠘⠋⠁⠈⠿⠿⠿⠛⠛⠉⠁⠀⣾⣿⣿⣿⣿
⣿⣇⠀⠈⠉⠉⠉⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿
⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠀⠀⠀⠀⠿⠟⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠠⣤⣤⣀⠀⠀⠀⠀⣴⢻⡿⠋⠀⡀⠀⠀⠀⠴⢿⣿⣿⣿⣿
⣿⣿⣿⣷⡄⠀⠀⠀⠙⠛⠘⠃⠀⠀⠀⠀⢀⣀⡀⣾⠇⠀⠀⠀⠀⠻⣿⣿⣿⣿
⣿⣿⣿⡿⠂⠀⠀⠘⣶⢠⣴⠀⣶⣶⣾⡇⣿⣿⡇⠟⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿
⣿⣿⡟⠁⠀⠀⠀⠀⠈⠸⢿⠀⣿⣿⣿⡇⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿
⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⢸⣿
⣿⣇⡄⣀⣰⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣾⣾⣾⣿
⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣀⣴⣶⣄⠀⢀⣠⣶⣦⡀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
ʀᴏᴄᴋᴇᴛ's     ᴛʀᴀsʜ     ᴍᴀᴄʜɪɴᴇ   
ᴘᴏᴋᴇᴍᴏɴ  ɢᴏᴏɴ  ᴘɪᴄ  ᴅᴏᴡɴʟᴏᴀᴅᴇʀ"""
# print(yellow + pikachu.replace('ᴘᴏᴋᴇᴍᴏɴ  ɢᴏᴏɴ  sᴏғᴛᴡᴀʀᴇ  ᴅᴏᴡɴʟᴏᴀᴅᴇʀ', blue + 'ᴘᴏᴋᴇᴍᴏɴ  ɢᴏᴏɴ  sᴏғᴛᴡᴀʀᴇ  ᴅᴏᴡɴʟᴏᴀᴅᴇʀ' + blue) + reset)
print(pikachu)

def process_url(url):
    # This function is called with the first URL in each message
    # Add your code here to process the URL


    hold = []
    new_domain = "a.4cdn.org"
    parsed_url = urlparse(url)
    path = parsed_url.path
    new_url = parsed_url._replace(netloc=new_domain)
    new_url = urlunparse(new_url) + ".json"
    first_directory = path.split('/')[1]
    thread = path.split('/')[3]
    response = requests.get(new_url)
    data = json.loads(response.text)
    result = "URL PROVIDED: "+url + "\n"
    for post in data['posts']:
        if 'sub' in post:
            sub = post['sub']
            # Connect to SQLite database and create table for post numbers
            conn = sqlite3.connect('posts.sqlite')
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS posts (no INTEGER PRIMARY KEY, thread INTEGER, url TEXT)')
            c.execute('CREATE TABLE IF NOT EXISTS threads (thread INTEGER PRIMARY KEY, title TEXT)')
            c.execute('SELECT * FROM threads WHERE thread=?', (thread,))
            if c.fetchone() is not None:
                print(f"Thread number {thread} is in the database already.")
            else:
                c.execute('INSERT INTO threads VALUES (?, ?)', (thread, sub))
                conn.commit()
            for post in data['posts']:
                if 'tim' in post and 'ext' in post:
                    tim = post['tim']
                    ext = post['ext']
                    no = post['no']
                    # Check if post number has already been posted
                    c.execute('SELECT * FROM posts WHERE no=?', (no,))
                    if c.fetchone() is not None:
                        print(f"Post number {no} has already been posted.")
                    else:
                        # Insert post number into database
                        url = "https://i.4cdn.org/"+ first_directory +"/"+ str(tim)+"" + ext
                        print(f"Posted: {url} in the discord.")
                        dir_name = "storage/pictures/"+thread
                        if not os.path.exists(dir_name):
                            os.makedirs(dir_name)
                        filename = os.path.join(dir_name, str(tim)+"" + ext)
                        urllib.request.urlretrieve(url, filename)
                        print(f"Downloaded and stored on backend.")
                        c.execute('INSERT INTO posts VALUES (?, ?, ?)', (no, thread, url))
                        conn.commit()
                        hold.append(url)
                        
    return hold

async def send_large_message(channel, content):
    for item in content:
        await channel.send(item)
        time.sleep(2)
    await channel.send("Thread up to date.")


@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        if message.content == "Thread up to date.":
            await asyncio.sleep(10)
            await message.delete()
        else:
            return

    if bot.user in message.mentions:
        # Delete the message
        await message.delete()
    # Search the message content for URLs
    urls = url_pattern.findall(message.content)
    
    if urls:
        # Pass the first URL to the process_url function
        wait = ["Please Wait"];
        await send_large_message(message.channel, wait)
        result = process_url(urls[0])
        await send_large_message(message.channel, result)

@bot.event
async def on_reaction_add(reaction, user):
    # Check if the reaction is an X emoji
    if reaction.emoji == "❌":
        # Get the number of members in the server
        member_count = len(reaction.message.guild.members)
        print(member_count)
        # Check if more than fourth of the members have reacted with the X emoji
        if reaction.count > member_count / 4:
            # Delete the message
            await reaction.message.delete()


bot.run(TOKEN)



