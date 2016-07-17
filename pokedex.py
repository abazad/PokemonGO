#!/user/bin/python

# Import the Modules
import discord
import urllib3
import asyncio
import sqlite3
import os

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
    
##### POKEDEX LOOKUP FUNCTION
##### RESPONSE TO COMMANDS:     !l
#####                           !lookup
#####                           !i
#####                           !info
#####                           !p
#####                           !pokedex
##### Pokedex Bot will first respond with the pokedex details
##### Professor Oak will then respond with the evolution details
##### Nurse Joy will finally respond with the egg hatching details
    
    # create the commands   
    if _command in ['!l', '!lookup', '!i', '!info', '!p', '!pokedex']:
        
        # save keys
        _pokemon = message.content.split(' ')[1].lower()
        
        # lookup the pokemon being passed
        _pokemon_details = f.lookup_pokemon(_pokemon)
        
        # check if pokemon exists
        if _pokemon_details != None:
            _exists = True
        else:
            _exists = False
            
        # if the pokemon exists, return the pokedex details
        if _exists == True:
            # save the results
            _number = _pokemon_details[0]
            _name = _pokemon_details[1].title()
            _description = _pokemon_details[4]
            _evolve = _pokemon_details[5]
            _types = _pokemon_details[6].split(', ')
            _egg = _pokemon_details[7]
            
            
            # compile the description message
            _content = '**{0}** (#{1:0>3}):\n'.format(_name, _number)
            _content = "{0}```{1}``` \n Types: ".format(_content, _description)
            for _each in _types:
                _content = "{0}`{1}` ".format(_content, _each.lower())
            _content = "{0}\n\n".format(_content)
            # add details about the evolution

            
            # Send the message pack the user
            yield from client.send_file(message.channel, '/Users/darcycartwright/Development/Python/Pokedex Bot/images/large/{0:0>3}.png'.format(_number), filename='{0:0>3}.png'.format(_number))
            yield from client.send_message(message.channel, _content)
            
            # Send the evolution data
            _content = '**Evolution:**\n'
            yield from client.send_message(message.channel, _content)    
            # Determine the correct evolution image
            _images = os.listdir('/Users/darcycartwright/Development/Python/Pokedex Bot/images/evolutions/')
            for _each in _images:
                if '{0:0>3}'.format(_number) in _each:
                    _image = _each
            yield from client.send_file(message.channel, '/Users/darcycartwright/Development/Python/Pokedex Bot/images/evolutions/{0}'.format(_image), filename=_image)
            try:
                _evolved = f.lookup_pokemon(_pokemon_details[3])
                _content = "```{1} evolves from {2} when {3} {1} candy are used.```\n".format(_content, _name, _evolved[1].title(), _evolved[5])
                yield from client.send_message(message.channel, _content)  
            except:
                pass
            try:
                _evolves = f.lookup_pokemon(_pokemon_details[2])
                _content = "```{1} evolves into {2} when {3} {1} candy are used.```\n".format(_content, _name, _evolves[1].title(), _evolve)
                yield from client.send_message(message.channel, _content)  
            except:
                pass          
            
            
            
            # end the function
            pass
        
        # if the pokemon doesn't exist, return an error message
        if _exists == False:
            yield from client.send_message(message.channel, 'No record for **{}** found within the Pokedex.'.format(_pokemon.title()))
            
            # end the function
            pass
        

        
##### FIND POKEMON FUNCTION
##### REPONSE TO COMMANDS:      !f
#####                           !find
#####                           !locate
#####                           !w
#####                           !where
#####                           !whereis

    # Set commands
    _commands = ['!f', '!find', '!locate', '!w', '!where', '!whereis']
    if _command in _commands:
        
        # end the function
        pass
        
##### HELP FUNCTION
##### RESPONSE TO COMMANDS:     !h
#####                           !help
##### Officer Jenny will PM the user with the help menu for the chatroom
    
    # Set commands
    _commands = ['!h', '!help']
    if _command in _commands:
        # end the function
        pass
    
        
# Create the example
def example_function(author, message):
    yield from client.send_message(message.channel, 'Say hello')

# Login to Discord as the Pokedex
bot = f.bot_info('pokedex')
client.run(bot['username'], bot['password'])
client.accept_invite('https://discord.gg/QwqqqQk')