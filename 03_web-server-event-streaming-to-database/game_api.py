# Setting up the file to execute in Python
#!/usr/bin/env python
import json
# Added to log events to Kafka.
from kafka import KafkaProducer
from flask import Flask, request
import random
# create a new flask instance
app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')

# Logs events to Kafka.  The default for encode is utf-8.
def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())

##################################################
# Functions
##################################################
# Function that randomly assigns sword purchases.
# The base sword is a templer sword.  There are different odds for purchasing other swords.
def sword_type():
    sword = "templer"
    rand = random.randint(1,100)
    if rand % 5 == 0:
        sword = "crusader"
        if rand % 25 == 0:
            sword = "hattori hanzo"
            if rand % 50 == 0:
                sword = "light saber"
    return sword

# This function attaches the cost of each sword to the purchase sword event.
def sword_cost(sword_type):
    if sword_type == "templer":
        cost = 5
    elif sword_type == "crusader":
        cost = 10
    elif sword_type == "hattori hanzo":
        cost = 25
    elif sword_type == "light saber":
        cost = 50
    else:
        cost = 0
    return cost

# Function for users to join a guild.
# There are five different guilds in the game.
def guild_assign():
    rand = random.randint(1,5)
    if rand == 1:
        guild = "Triad"
    elif rand == 2:
        guild = "Hellforge"
    elif rand == 3:
        guild = "Blueblades"
    elif rand == 4:
        guild = "Bouldergarde"
    else:
        guild = "Madvale"
    return guild

##################################################
# Events
##################################################
# Flask works with the app.route decorators.
# Each app.route decorator has a different name to distinguish different events.
# Inside each function we log the event to Kafka.  Inside log_to_kafka the topic name is specified.
# The business logic is returning the response.

# This is the default route. When the route is called the function is executed.
# I did not create a stream for this event, but I left it in the game for future use.
@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"

# This is the sword route, it has an event type, sword type, and sword cost properties.
# When the sword is purchased it is assigned to a specific user.
# The function outputs the response "Sword Puchased!" to the terminal.
@app.route("/purchase_a_sword")
def purchase_a_sword():
    dPSword1 = {'event_type': 'purchase_sword',
                'sword_type': sword_type()}
    dPSword2 = {'sword_cost': sword_cost(dPSword1['sword_type'])}
    purchase_sword_event = dPSword1.copy()
    purchase_sword_event.update(dPSword2)
    log_to_kafka('events', purchase_sword_event)
    return "Sword Purchased!\n"

# This is the knife route that is not used but available for future use.
@app.route("/purchase_a_knife")
def purchase_a_knife():
    purchase_knife_event = {'event_type': 'purchase_knife',
                            'description': 'very sharp knife'}
    log_to_kafka('events', purchase_knife_event)
    return "Knife Purchased!\n"

# This is the join guild route, it has an event type and a guild (name of the guild) properties. 
@app.route("/join_guild")
def join_guild():
    guild = guild_assign()
    join_guild_event = {'event_type': 'join_guild',
                        'guild':guild}
    log_to_kafka('events', join_guild_event)
    text1 = "You have joined "
    text2 = "!"
    text0 = text1 + guild + text2
    return text0 + "\n"

