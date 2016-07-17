#!/user/bin/python

# Import the Modules
import discord
import urllib3
import asyncio
import sqlite3

import functions as f

# Disable the SSL warning printed to the console
urllib3.disable_warnings()

# Establish a connection with discord
client = discord.Client()

# Connect to the Pokedex database
db = sqlite3.connect('pokedex.db')
cursor = db.cursor()

# Perform actions on messages
@client.async_event
def on_message(message):
    author = message.author
    commands = ['!f ', '!found', '!c ', '!caught']
    if message.content.startswith('!test'):
        example_function(author, message)
        yield from client.send_message(message.channel, 'Say hello')
    



# Login to Discord as the Pokedex
bot = f.bot_info('joy')
client.run(bot['username'], bot['password'])
client.accept_invite('https://discord.gg/QwqqqQk')