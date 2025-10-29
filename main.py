import discord
import os # default module
from dotenv import load_dotenv
import random

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

# When the user mentions the bot, respond with a random string from a list of responses
@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        responses = [
            "Hello!",
            "Hi there!",
            "Greetings!",
            "Salutations!",
            "Howdy!"
        ]
        await message.channel.send(random.choice(responses))

bot.run(os.getenv('TOKEN')) # run the bot with the token