import discord
from discord.ext import commands
import asyncio
import json
import datetime
import time
import random

def get_prefix(bot, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]  

Farben = [0xFF0000, 0x88FF00, 0xFFFF00, 0xFF8800, 0x8800FF, 0x48EDDD]

start_time = time.time()

token = "Your Token" #Your Token

bot = commands.Bot(command_prefix=get_prefix, case_intensive=True, intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user}')
    print(f'{bot.user.id}')
    bot.loop.create_task(status_task())

async def status_task():
  while True:    
    await bot.change_presence(activity=discord.Game('>>help'), status=discord.Status.online)
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Game('coded by x10 Lukas#9543'), status=discord.Status.online)
    await asyncio.sleep(10)  

@bot.event
async def on_guild_join(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)] = '>>'

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes,f)  

@bot.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes[str(ctx.guild.id)] = prefix

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes,f) 

  embed = discord.Embed(description=f"The prefix was changed to: {prefix}", color=random.choice (Farben))
  await ctx.send(embed=embed) 

#Help-cmd#
@bot.command()
async def help(ctx):
  with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

  pre = prefixes[str(ctx.guild.id)]

  embed = discord.Embed(title="{} | Help Commands".format(ctx.message.guild.name), description=f"**Prefix:** `{pre}`",color=random.choice (Farben))
  embed.set_thumbnail(url=ctx.guild.icon_url)
  embed.add_field(name="__ALL__", value="> `help`, `botinfo`, `ping`, `severinfo`, `userinfo`, `avatar`", inline=False)   
  embed.add_field(name="__MOD__", value="> `changprefix`, `clear`, `say`, `poll`, `kick`, `ban`, `unban + User#0000`", inline=False)
  embed.add_field(name="_**BOT BY:**_", value=f"> <@440251035773173767> `x10 Lukas`", inline=False)
  embed.set_footer(text=f"{ctx.guild.name}",icon_url=f"{ctx.guild.icon_url}")
  await ctx.send(embed=embed) 

@bot.command(pass_context=True, aliases=['i', 'info'])
async def botinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member

    with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

    pre = prefixes[str(ctx.guild.id)]

    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))

    embed = discord.Embed(title="", description="", color=random.choice (Farben))
    embed.set_author(name="Information about {}".format(ctx.message.guild.name), icon_url=f"{ctx.guild.icon_url}")
    embed.add_field(name="🤖 BOT TAG", value=f"`{ctx.guild.name}`", inline=True)
    embed.add_field(name="🤖 BOT VERSION", value=f"`1.0.0`", inline=True)  
    embed.add_field(name="🤖 PYTHON.PY VERSION", value="`Python 3.9.1`", inline=True)  
    embed.add_field(name="⌚️ UPTIME", value=text, inline=True)  
    embed.add_field(name="📶 PING", value=f"`{round(bot.latency * 10000)} ms`", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="📁 Server count", value=f"`1`", inline=True)
    embed.add_field(name="📁 Total Members", value=f"`{len(list(ctx.guild.members))}`", inline=True)
    embed.add_field(name="📁 Commands Amount", value=f"`20`", inline=True)
    embed.add_field(name="__**CUSTOM SETUPS:**__", value="\u200b", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="📌 SERVER PREFIX", value=f"`{pre}`", inline=True)
    embed.add_field(name="⏳ BOT CHANNELS", value=f"**not setup**", inline=True)
    embed.add_field(name="⚙️ Amount of Commands used", value=f"**not setup**")
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="_**BOT BY:**_", value=f"> <@440251035773173767> `x10 Lukas`", inline=False)
    embed.set_footer(text=f"{ctx.guild.name}",icon_url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(color=random.choice (Farben))
    embed.set_author(name="{} Serverinformation".format(ctx.message.guild.name), icon_url=f"{ctx.guild.icon_url}")
    embed.set_thumbnail(url=ctx.message.guild.icon_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Server Owner", value=f"`{ctx.guild.owner}`", inline=True)
    embed.add_field(name="Region", value=f"`{ctx.guild.region}`", inline=True)
    embed.add_field(name="Time Created", value=f"`{ctx.guild.created_at.strftime('%d/%m/%Y, %H:%M:%S')}`", inline=True)
    embed.add_field(name="Boost Trier", value=f"`{ctx.guild.premium_tier}`", inline=True)
    embed.add_field(name="Channel Count", value=f"`{len(list(ctx.guild.channels))}`", inline=True)
    embed.add_field(name="Text Channels:", value=f"`{len(list(ctx.guild.text_channels))}`", inline=True)
    embed.add_field(name="Voice Channels:", value=f"`{len(list(ctx.guild.voice_channels))}`", inline=True)
    embed.add_field(name="Member Count", value=f"`{len(list(ctx.guild.members))}`", inline=True)
    embed.add_field(name="Regular Emojis", value=f"`{len(list(ctx.guild.emojis))}`", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=False)
    embed.add_field(name="_**BOT BY:**_", value=f"> <@440251035773173767> `x10 Lukas`", inline=False)
    embed.set_footer(text=f"{ctx.guild.name}",icon_url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed) 

@bot.command(aliases=['uinfo'])
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(color=random.choice (Farben), timestamp=ctx.message.created_at)
    embed.set_author(name=f"Information about - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"{ctx.bot.user.name}", icon_url="")
    embed.add_field(name="TAG:", value=f"`{member}`,{member.mention}", inline=True)
    embed.add_field(name="ID:", value=f"`{member.id}`", inline=True)
    embed.add_field(name="Is a BOT:", value=f"`{member.bot}`", inline=True)
    embed.add_field(name="Joined Discord:", value=f"`{member.created_at.strftime('%d/%m/%Y, %H:%M:%S')}`", inline=True)
    embed.add_field(name="Presence:", value=f"`{member.activity}`", inline=True)
    embed.add_field(name="Status:", value=f"`{member.status}`", inline=True)
    embed.add_field(name="ROLLEN:", value=" ".join([role.mention for role in roles]), inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=False)
    embed.add_field(name="_**BOT BY:**_", value=f"> <@440251035773173767> `x10 Lukas`", inline=False)
    embed.set_footer(text=f"{ctx.guild.name}",icon_url=f"{ctx.guild.icon_url}") 
    await ctx.send(embed=embed)    

@bot.command()
async def avatar(ctx):
  embed = discord.Embed(title=f"{ctx.author}'s Avatar", color=random.choice (Farben))
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  embed.set_image(url=f"{ctx.author.avatar_url}")
  embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
  await ctx.send(embed=embed)

#Mod-Commands#
@bot.event
async def on_command_error(ctx, error, amount=1):

  with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

  pre = prefixes[str(ctx.guild.id)]

  if isinstance(error,commands.CommandNotFound):
    embed = discord.Embed(description=f"❗️  **| {ctx.author.mention} You have entered the wrong command!**", color=discord.Colour.red())
    await ctx.send(embed=embed)
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=amount+1)
    await asyncio.sleep(1)
    embed = discord.Embed(description=f"**Type `{pre}help` for more Information**", color=0xfdb917)
    await ctx.send(embed=embed)
    
  if isinstance(error,commands.MissingPermissions):
    embed = discord.Embed(description=f"❗️  **| {ctx.author.mention} You do not have enough permissions!**", color = discord.Colour.red())
    await ctx.send(embed=embed)  

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
  embed = discord.Embed(title="{}".format(ctx.message.guild.name), description=f"{amount} Messages was deleted", color=random.choice (Farben))
  await ctx.send(embed=embed)
  await asyncio.sleep(2)
  await ctx.channel.purge(limit=amount+2)

@bot.command(pass_context=True)
@commands.has_guild_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="no reason given"):
  embed = discord.Embed(title="{}".format(ctx.message.guild.name), description=f"You were kicked from {ctx.guild.name} because " +reason, color=discord.Colour.red())
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
  embed.timestamp = datetime.datetime.utcnow()  
  await member.send(embed=embed)

  embed = discord.Embed(description=f"{member.mention} got kicked from the server by {ctx.author.mention}", color=discord.Colour.red())
  embed.set_author(name=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
  embed.timestamp = datetime.datetime.utcnow()
  await ctx.send(embed=embed)
  await member.kick(reason=reason)

@bot.command(pass_context=True)
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="no reason given"):
  embed = discord.Embed(title="{}".format(ctx.message.guild.name), description=f"You were banned from {ctx.guild.name} because" +reason, color=discord.Colour.red())
  embed.timestamp = datetime.datetime.utcnow()  
  await member.send(embed=embed)
  await member.ban(reason=reason)     
            
@bot.command(pass_context=True)
@commands.has_guild_permissions(ban_members=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_disc = member.split('#')

  for banned_entry in banned_users:
    user = banned_entry.user

    if(user.name, user.discriminator)==(member_name,member_disc):

      await ctx.guild.unban(user)
      embed = discord.Embed(title="{}".format(ctx.message.guild.name), description=member_name +" has been unbanned!", color=random.choice)
      await ctx.send(embed=embed)
      return

  embed = discord.Embed(title="{}".format(ctx.message.guild.name), description=member_name +" was not found", color=discord.Colour.red())
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_guild_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, text):
  embed=discord.Embed(title="{} | Warning".format(ctx.message.guild.name), description=f"This is a warning to you {member}\n\n Reason: {text}", color=0xfdb917)
  embed.set_thumbnail(url=f"{member.guild.icon_url}")
  await member.send(embed=embed)

@bot.command(aliases=['p'])
async def ping(ctx):
    embed = discord.Embed(description=f"`{round(bot.latency * 10000)} ms`", color=random.choice (Farben))
    embed.set_author(name=f"PING", icon_url="https://cdn.discordapp.com/emojis/798953395062702151.png?v=1")
    embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed) 

@bot.command()
@commands.has_permissions(manage_messages=True)
async def poll(ctx, *, message):
  embed = discord.Embed(description=f"{message}", color=random.choice (Farben))
  embed.set_author(name=f"{ctx.guild.name} | Poll", icon_url=f"{ctx.guild.icon_url}")
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
  msg=await ctx.channel.send(embed=embed)
  await msg.add_reaction('✅')
  await msg.add_reaction('❌') 

@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, message):
  embed = discord.Embed(description=f"{message}", color=random.choice (Farben))
  embed.set_author(name=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
  msg=await ctx.channel.send(embed=embed)
    
bot.run(token)  
