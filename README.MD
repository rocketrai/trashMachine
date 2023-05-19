# Rocket's Trash Machine
The main purpose of this app is to allow users to download 4chan thread images fast and effectivly then post them into a discord room.

## Setup
First you need to make a .env file. Copy the example and enter your key.

`cp .env.example .env`

Next install the requirements with:

`pip install -r requirements.txt`

Next all you have to do it run the bot and invite your bot to your server. 

## Bot use
Run the bot with `ptyhon3 robust.py`

After that just @ the bot and link it to your 4chan thread you want to scrape. 
The bot will then scrape the thread and post all the images in the thread to the channel. 

The bot will make sure not to repost images it has posted already by making a sqlite database with posted images. Soon the boot will also have a self host option that will post self hosted version of the pictures to discord instead of the 4chan links.
