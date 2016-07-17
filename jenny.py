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
    # store the message parameters
    _author = message.author
    _command = message.content.split(' ')[0].lower()
    
##### HELP FUNCTION
##### RESPONSE TO COMMANDS:     !h
#####                           !help
##### Officer Jenny will PM the user with the help menu for the chatroom
    
    # Set commands
    _commands = ['!h', '!help']
    if _command in _commands:
        _content = '**Help Menu:**\n'
        _content = "{} Search for a Pokemon's details in the Pokedex:\n".format(_content)
        _content = '{} ```Use one of the following listed commands followed by a Pokemons name or number to view the pokedex entry.\n```'.format(_content)
        _content = '{} `!p` or `!pokedex`\n'.format(_content)
        _content = '{} *Example:*\n'.format(_content)
        _content = '{} `!pokedex Pikachu` or `!p 25`\n'.format(_content)
        _content = '{} \n'.format(_content)
        yield from client.send_message(message.author, _content)
        # end the function
        pass

# Welcome new members to the room
@client.async_event
def on_join(member):
    # Welcome the member to the group
    yield client.send_message(member.server, 'Welcome <@{}>!'.format(member.id))
    # Send them a private message asking they they need help.
    yield client.send_message(member.server, 'Welcome <@{}>!\n\nIf you get lost, or need any help with commands in the chat, just type in `!help`!\n')
    
    
    
# Login to Discord as the Pokedex
bot = f.bot_info('jenny')
client.run(bot['username'], bot['password'])
client.accept_invite('https://discord.gg/QwqqqQk')