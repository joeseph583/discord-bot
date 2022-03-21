import os
import re
import requests
from discord.ext import commands
from dotenv import load_dotenv

# discord bot

load_dotenv()

CHANNEL = os.getenv('DISCORD_CHANNEL')
USER = os.getenv('DISCORD_USER')
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '!')

# verifies bot is logged in

@client.event
async def on_ready():
    print('Bot is logged in.')

# checks if message is from the correct channel and from the correct user

@client.event
async def on_message(message):
    if str(message.author) == str(USER) and str(message.channel) == str(CHANNEL):
        body = str(message.content)

        # extract contract address

        p1 = r'[^/]\b' + '0x' + '........................................' + r'\b'
        match = re.findall(p1, body)
        if len(match) == 1:
            contractAddress = match[0].replace(' ', '')
            print(contractAddress)

            # send SMS / purchase tokens / etc. here:

client.run(TOKEN)