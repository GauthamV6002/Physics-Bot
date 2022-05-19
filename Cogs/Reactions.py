#stupid spahgetti code im ded

import discord
from discord.ext import commands
from discord.utils import get
from replit import db

if not db["reactionRoleMsgId"]:
  db["reactionRoleMsgId"]= 962442617700876338

if not db["reactionRoles"]:
  db["reactionRoles"]= ""

#random emojis i can change these later or whatever
reactionsRoleEmojis = ["❓", "⛔", "🤣", "🩳", "💰", "😭"]
reactionRoles = []

class Reactions(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context=True)
  # @commands.has_role("Admin")
  async def reactionRoleCreate(self, ctx, *, roles=None):
    
    #handle role-choosing
    if roles:
      roles_strs = roles.split(", ")
      roles = [get(ctx.guild.roles, name=r) for r in roles_strs]
      
      if None in roles:
        #some spagetti code woohoo
        await ctx.send(f"Hmmm... \n I couldn't find the role ``{roles_strs[roles.index(None)]}``. Make sure the roles you are listing are comma-seperated and spelled correctly.")
        return
    else:
      roles = ctx.guild.roles

    #make and send embed
    embed=discord.Embed(
      title="Reaction Roles", 
      description="React to this message to recieve roles.",
      color=discord.Color.blue()
    )

    for index, role in enumerate(roles):
      embed.add_field(name=f"{str(role)}: ", value=reactionsRoleEmojis[index], inline=False)
    
    message = await ctx.send(embed=embed)
    for emoji in reactionsRoleEmojis[:len(roles)]:
      await message.add_reaction(emoji)

    db["reactionRoleMsgId"] = message.id
    db["reactionRoles"] = roles_strs

  
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    guild = await self.bot.fetch_guild(payload.guild_id)
    reactionRoleMsgId = db["reactionRoleMsgId"]
    reactionRoles = [get(guild.roles, name=r) for r in db["reactionRoles"]]
    
    if reactionRoleMsgId == payload.message_id:
      member = payload.member
      emoji = payload.emoji.name
      
      role = reactionRoles[reactionsRoleEmojis.index(emoji)]
      await member.add_roles(role)
  
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    reactionRoleMsgId = db["reactionRoleMsgId"]
    guild = await self.bot.fetch_guild(payload.guild_id)
    reactionRoles = [get(guild.roles, name=r) for r in db["reactionRoles"]]
    
    if reactionRoleMsgId == payload.message_id:
      
      member = await guild.fetch_member(payload.user_id)
      emoji = payload.emoji.name

      role = reactionRoles[reactionsRoleEmojis.index(emoji)]
      if member is not None:
        await member.remove_roles(role)
    
def setup(bot):
  bot.add_cog(Reactions(bot))