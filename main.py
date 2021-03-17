import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix=
"", case_insensitive=True, intents_members=True)

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('Try typing ping.'))
	print("Ping Pong Bot is ready.")

@client.command()
async def ping(ctx):
	await ctx.send("pong")

@client.command()
async def pong(ctx):
	await ctx.send("ping")

client.run("TOKEN")

#Note: Line 21 is usually where the token goes (instead of TOKEN) but for obvious reasons I have censored it.
