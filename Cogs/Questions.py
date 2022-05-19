from discord.ext import commands
import discord
from FormulaQGen import QUESTION_GENERATOR_LIST
import random

class Questions(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['fq', 'formula_question', 'question', 'formulaQuestion'])
  async def formulaQ(self, ctx, *, category=None):
    if not(category in QUESTION_GENERATOR_LIST) and category != None:
      await ctx.send("Invalid Category. Valid categories are ``kinematics``, ``circular motion``, ``work/energy``, ``harmonic motion``")
      return
    
    if category != None:
      filled_values = random.choice(QUESTION_GENERATOR_LIST[category]).question_values()
    else: 
      filled_values = random.choice(random.choice(list(QUESTION_GENERATOR_LIST.values()))).question_values()
    print(filled_values)
    removed = random.choice(list(filled_values))
    removed_value = filled_values[removed]
    del filled_values[removed]
    
    embed=discord.Embed(title="Physics Equation Questioner", description="Your next message will be considered an answer. Sig digs & units still in development :(, So just round to 2 decimal places.", color=discord.Color.green())
    for key, value in filled_values.items():
      embed.add_field(name=f"{key}=", value=value, inline=True)
    embed.add_field(name="Solve for:", value=removed, inline=False)

    await ctx.send(embed=embed)
    message = await self.bot.wait_for("message", check=lambda m: m.author == ctx.author)
    
    if float(message.content) == float(removed_value):
      await message.add_reaction("✅")
    else:
      await message.add_reaction("❌")
      await ctx.send(f"Hmmm, looks like something went wrong! The correct answer was ``{removed_value}``.")
    
    
    
		

def setup(bot):
	bot.add_cog(Questions(bot))