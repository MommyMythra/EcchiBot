import nextcord
import os
import random
import asyncpraw
from replit import db
from nextcord.ext import commands


intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix = "$", intents=intents)

elf_slut=[
  "Plunder my dungeon, Hero!",
  "Allow me to pull your Excalibur from your stone...",
  "Oh! You've critically hit my clit!",
  "I could use a big orc cock right about now.",
  "I hope my organs get rearranged by a massive dick tonight.",
  "What am I doing tonight? Why don't you rent a room at the inn and find out...",
  "You can stay, but your clothes must go.",
  "Want to see what I can do with my mage hand?",
  "My record? 7 inch diameter... want to see if I can fit 8?"
]

def add_suggest(userID, suggest):
  print(userID)
  if userID in db.keys():
    add = db[userID]
    add.append(suggest)
    db[userID] = add
  else:
    print("die")
    db[userID] = [suggest]

def print_suggest(userID):
  msg = db[userID].value
  return msg

def delete_suggest(userID, index):
  rem = db[userID]
  if len(rem) > index:
    del rem[index]
  db[userID] = rem

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))    

@bot.event
async def on_member_join(member):
  guild = member.guild
  if guild.system_channel is not None:
    await guild.system_channel.send("Welcome to the office " + member.mention + "!")
  else:
    print("fuck")

@bot.command()
async def tease(ctx):
  desire = random.choice(elf_slut)
  await ctx.send(desire)

@bot.command()
async def taskhelp(ctx):
  helpmsg = "Hello and welcome to the office! I see you're looking for the tasks I can handle! \nMy current prefix is: " + bot.command_prefix + "\n"
  helpmsg = helpmsg + "I support the following tasks as your intern:\n"
  helpmsg = helpmsg + "\t- taskhelp\n"
  helpmsg = helpmsg + "\t- tease\n"
  helpmsg = helpmsg + "\t- suggest [@user] [\"message\"]\n"
  helpmsg = helpmsg + "\t- mySug\n"
  helpmsg = helpmsg + "\t- remSug [Suggestion #]\n"
  helpmsg = helpmsg + "\t- memePiece [hot/new/top]\n"
  helpmsg = helpmsg + "\t- rap\n"
  helpmsg = helpmsg + "I hope To be of future assistance!"
  await ctx.send(helpmsg)

@bot.command()
async def suggest(ctx, arg1, *, arg2):
  if(len(ctx.message.mentions) == 0):
    await ctx.send("I'm sorry, but our guild doesn't have a... \"" + arg1 + "\"")
  else:
      suggestion = arg2
      add_suggest(str(ctx.message.mentions[0].id), suggestion)
      if(ctx.message.mentions[0].nick == None):
        await ctx.send("I have added the suggestion to " + ctx.message.mentions[0].name + "'s report")
      else:
        await ctx.send("I have added the suggestion to " + ctx.message.mentions[0].nick + "'s report")
      
@suggest.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("I'm sorry, but your request is improper. Try `" + bot.command_prefix + "suggest [@user] [\"message\"]`")

@bot.command()
async def mySug(ctx):
  if(str(ctx.message.author.id) in db.keys()):
      sug = print_suggest(str(ctx.message.author.id))
      if(ctx.message.author.nick == None):
          sugFin = "Hello! Here is the current full report \n`Full report for " + ctx.message.author.name + ":\n"
          for i in range(len(sug)):
            sugFin = sugFin + str(i+1) + ") " + sug[i] + "\n"  
          sugFin = sugFin + "`Have a pleasant day!"
          await ctx.send(sugFin)
      else:
        sugFin = "Hello! Here is the current full report \n`Full report for " + ctx.message.author.nick + ":\n"
        for i in range(len(sug)):
          sugFin = sugFin + str(i+1) + ") " + sug[i] + "\n"  
        sugFin = sugFin + "`Have a pleasant day!"
        await ctx.send(sugFin)
  else:
    await ctx.send("There are no records on file for this user!")

@bot.command()
async def remSug(ctx, arg1):
  if(str(ctx.message.author.id) in db.keys()):
    delete_suggest(str(ctx.message.author.id), int(arg1)-1)
    sug = print_suggest(str(ctx.message.author.id))
    if(ctx.message.author.nick == None):
      sugFin = "Hello! Here is the current full report \n`Full report for " + ctx.message.author.name + ":\n"
      for i in range(len(sug)):
        sugFin = sugFin + str(i+1) + ") " + sug[i] + "\n"  
      sugFin = sugFin + "`Have a pleasant day!"
      await ctx.send(sugFin)
    else:
      sugFin = "Hello! Here is the current full report \n`Full report for " + ctx.message.author.nick + ":\n"
      for i in range(len(sug)):
        sugFin = sugFin + str(i+1) + ") " + sug[i] + "\n"  
      sugFin = sugFin + "`Have a pleasant day!"
      await ctx.send(sugFin)
  else:
    await ctx.send("There are no records on file for this user!")

@remSug.error
async def info_error2(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("I'm sorry, but your request is improper. Try `" + bot.command_prefix + "remSug [Suggestion #]`")

@bot.command()
async def otherSug(ctx, arg1):
  if(str(ctx.message.mentions[0].id) in db.keys()):
    sug = print_suggest(str(ctx.message.mentions[0].id))
    if(ctx.message.mentions[0].nick == None):
      sugFin = "Hello! Here is the current full report \n`Full report for " + ctx.message.mentions[0].name + ":\n"
      for i in range(len(sug)):
        sugFin = sugFin + str(i+1) + ") " + sug[i] + "\n"  
      sugFin = sugFin + "`Have a pleasant day!"
      await ctx.send(sugFin)
    else:
      sugFin = "Hello! Here is the current full report \n`Full report for " + ctx.message.mentions[0].nick + ":\n"
      for i in range(len(sug)):
        sugFin = sugFin + str(i+1) + ") " + sug[i] + "\n"  
      sugFin = sugFin + "`Have a pleasant day!"
      await ctx.send(sugFin)
  else:
    await ctx.send("There are no records on file for this user!")
  

@otherSug.error
async def info_error3(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("I'm sorry, but your request is improper. Try `" + bot.command_prefix + "otherSug [@user]`")
      
@bot.command()
@commands.check_any(commands.has_role(923041228226981909), commands.has_role(923041156592451635), commands.is_owner())
async def adminMSG(ctx, cName: nextcord.TextChannel, *, msg):
    await cName.send(msg)


@adminMSG.error
async def info_error4(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("I'm sorry, but your request is improper. Try `" + bot.command_prefix + "adminMSG [#channel]` [msg]")
  

#for my memePiece meme grabber
reddit = asyncpraw.Reddit(
    client_id="client_id",
    client_secret="client_secret",
    user_agent="my user agent")


@bot.command()
async def memePiece(ctx, browse = "new"):
    sub = await reddit.subreddit("memePiece")
    posts = []

    if browse == "hot":
      big = sub.hot(limit = 100)
    elif browse == "new":
      big = sub.new(limit = 100)
    elif browse == "top":
      big = sub.top(limit = 100)

    async for submission in big:
        posts.append(submission)
    random_sub = random.choice(posts)

    name = random_sub.title
    url = random_sub.url

    em = nextcord.Embed(title = name+"\n"+url)
    
    em.set_image(url = url)

    await ctx.send("I found this one piece meme while scrolling reddit...")
    await ctx.send(embed = em)

@memePiece.error
async def info_error5(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("I'm sorry, but your request is improper. Try `" + bot.command_prefix + "memePiece [hot/new/top]")

@bot.command()
async def rap(ctx):
  await ctx.send("The pirate rap... as requested: https://www.youtube.com/watch?v=RSe8D2wfGKI")
  

bot.run(os.getenv('TOKEN'))
