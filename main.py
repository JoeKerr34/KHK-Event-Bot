import discord
from discord.ext import commands

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())


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


client.run('MTIxNTg0MjI1ODkzOTU0MzU2Mw.GNeAXs.m0nn8Y2uEe4G1-VPVYe0DsBbn-FLxv4JYQTtdE')
