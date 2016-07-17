#!/user/bin/python

# Import the Modules
import sqlite3

# Function to lookup user details
def bot_info(name):
    # Connect to the Pokedex database
    _db = sqlite3.connect('pokedex.db')
    _cursor = _db.cursor()
    # Query the user database
    _query = "SELECT * FROM users WHERE user_name='{}'".format(name)
    _cursor.execute(_query)
    _result = _cursor.fetchone()
    _request = dict()
    _request['username'] = _result[0]
    _request['password'] = _result[1]
    # Close the connection to the database
    _db.close()
    return _request


# Functino to lookup a pokemon
def lookup_pokemon(name):
    # Connect to the Pokedex database
    _db = sqlite3.connect('pokedex.db')
    _cursor = _db.cursor()
    
    # Determine if the pokemon is being searched by number of name
    if name.isdigit() == True:
        _column = 'id'
    else:
        _column = 'pokemon_name'
    
    # Lookup the pokemon being passed=
    _query = "SELECT * FROM pokemon WHERE {0}='{1}'".format(_column, name)
    _cursor.execute(_query)
    _result = _cursor.fetchone()
    
    # Return the result
    return _result
    