import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())

config_file = open("config.json")
config = json.load(config_file)


@client.event
async def on_ready():
    print("Bot is now ready for use")
    print("------------------------")


# TODO: Implement the event listing
# Shows the events in the current week
@client.command()
async def events(ctx):
    # Display the events for the week
    await ctx.send("Here are the events for the week")


client.run(config["bot_token"])
