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
            "Ja, deze poost is gefeitencheckt door echte idioten",
            "Ja, deze poost is gefeitencheckt door echte patrioten",
            "Ja, dit gaat hard",
            "Ja, mijn bronnen zeggen mij van wel",
            "Wij gaan jou jou doodslaan",
            "Ik denk het wel",
            "Volgens mij is dit waar",
            "Volgens mij is dit wanneer",
            "Volgens mij is dit waarom",
            "Hoe durf je dit te vragen",
            "Bobbie jij soepkip je hebt Grok gevraagd",
            "Moet je niet aan mij vragen",
            "Ik weet wat je vraagt maar ik zeg het lekker niet",
            "Heb ik geen zin in",
            "Ik wordt daar zo moe van van zeggen of het waar is, ik doe niet meer mee, ik ga slapen",
            "The Bluetooth Device is Ready To Pair",
            "Waarom vraag je mij?",
            "Vraag het aan @pika1106 ofzo.",
            "Wat een ongeloofelijke kutvraag",
            "Nee, dit is Grok",
            "Dit is niet echt.",
            "Dit is nep",
            "Dit hebben de mensen van de redactie helemaal zelf bedacht",
            "Dit hebben we verzonnen",
            "Waarom zou je ooit denken dat dit echt was?",
            "Lees de vraag eens hardop",
            "Waarom zijn de bananen grok?",
            "Jou Grok rechten zijn bij deze afgenomen.",
            "Nee dit is niet echt.",
            "Voor de zoveelste keer, nee.",
            "Hak een boom om met een haring en vraag het nog eens.",
            "Kun je die vraag herhalen? Ik begreep het niet helemaal."
        ]
        await message.channel.send(random.choice(responses))

bot.run(os.getenv('TOKEN')) # run the bot with the token