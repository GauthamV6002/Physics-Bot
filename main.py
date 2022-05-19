import discord
from discord.ext import commands
from keep_alive import keep_alive
import os


intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.

bot = commands.Bot(command_prefix = "_", intents=intents)
TOKEN = os.environ['TOKEN']

#COGS
bot.load_extension("Cogs.Utilities")
bot.load_extension("Cogs.Reactions")
bot.load_extension("Cogs.Questions")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("The command you used is missing arguments!")

# @bot.command()
# async def clearHistory(ctx):
#   messages = await channel.history(limit=200).flatten()

@bot.event
async def on_ready():
  print('Successful Login! 🚀')
  await bot.change_presence(status=discord.Status.online, activity = discord.Game('| _help'))

keep_alive()

bot.run(TOKEN)

