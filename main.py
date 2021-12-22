import nextcord
import os
import requests
import json
import random
import logging

client = nextcord.Client()
elf_slut=[
  "Plunder my dungeon, Hero!",
  "Allow me to pull your Excalibur from your stone...",
  "Oh! You've critically hit my clit!",
  "I could use a big orc cock right about now.",
  "I hope my organs get rearranged by a massive dick tonight.",
  "What am I doing tonight? Why don't you rent a room at the inn and find out...",
  "You can stay, but your clothes must go.",
  "Want to see what I can do with my mage hand?",
  "My record? 7 inch diameter... want to see if I can fit 8?"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)
    if message.content.startswith('$slut'):
      desire = random.choice(elf_slut)
      await message.channel.send(desire)

client.run(os.getenv('TOKEN'))
