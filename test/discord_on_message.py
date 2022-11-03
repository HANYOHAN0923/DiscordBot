# This example requires the 'message_content' intent.
# ref: https://discordpy.readthedocs.io/en/stable/quickstart.html
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('How are you'):
        await message.channel.send('I\'m fine')
 
client.run(TOKEN)