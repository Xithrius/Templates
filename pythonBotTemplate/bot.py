#-----------------------------------------------------------------------------#
# Libraries
#-----------------------------------------------------------------------------
import discord
from discord.ext import commands as comms
import os
import json
import platform
import sys
#/////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------#
# Different paths for different operating systems
#-----------------------------------------------------------------------------
def pathing(object):
    if platform.system() == "Windows":
        return f"{os.path.dirname(os.path.realpath(__file__))}\\{object}"
    elif platform.system() == "Linux":
        return f"{os.path.dirname(os.path.realpath(__file__))}/{object}"
#/////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------#
# Main commands and events
#-----------------------------------------------------------------------------
class MainCog():
    def __init__(self, bot):
        self.bot = bot

    @comms.command()
    async def help(self, ctx):
        ctx.send(embed=embed)

    @comms.command()
    async def exit(self, ctx):
        if await ctx.bot.is_owner(ctx.author):
            print("Exiting...")
            await self.bot.logout()
        else:
            await ctx.send(f"{ctx.author.mention} you cannot do this")
#/////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------#
# Checking files
#-----------------------------------------------------------------------------
def initErrorCheck():
    try:
        with open(pathing('login.json'), "r") as f:
            login = json.load(f)
            return [login["discord"]["owner_id"], login["discord"]["bot_token"]]
    except FileNotFoundError:
        errorMessage("The file login.json cannot be found.", sys.exc_info())
        with open(pathing('login.json'), "r+") as f:
            owner_id = input("Input discord user owner for owner_id: ")
            bot_token = input("Input discord bot token for bot_token: ")
            tokens = {
            "discord": [owner_id, bot_token]
            }
            json.dump(logins, f)
    except IndexError:
        errorMessage("The file login.json has been modified and cannot be read.", sys.exc_info())
#/////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------#
# When there is an error, this will be called and shown to console.
#-----------------------------------------------------------------------------
def errorPrompt(string, type=None):
    if type != None:
        x = f"#{'/' * len(string)}#"
        print(f"{x}\n{type}:\n{string}\n{x}")
    else:
        x = f"#{'/' * len(string)}#"
        print(f"{x}\n{string}\n{x}")
#/////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------#
# Input checking for all the needs
#-----------------------------------------------------------------------------
def inputTest(string):
    check = True
    while check:
        for i in range(len(string)):
            if string[i] == '[':
                forwardBracket = i + 1
            elif string[i] == ']':
                backwardBracket = i
        options = (string[forwardBracket:backwardBracket]).split("/")
        print(string, end='', flush=True)
        In = input(" ")
        if In in options:
            return In
            check = False
        else:
            print(f"Input does not match options of {', '.join(str(y) for y in options)}")
#/////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------#
# The event tells by console when the bot is ready to be used.
#-----------------------------------------------------------------------------
class BotClient(comms.Bot):
    async def on_ready(self):
        print(f"Logging in as {bot.user}")
        print(f"{bot.user} ID: {bot.user.id}")
        print("Awaiting...")
#/////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------#
# Calling of bot functions
#-----------------------------------------------------------------------------
logins = initErrorCheck()
try:
    bot = BotClient(command_prefix = "$", owner_id = logins[0])
    bot.remove_command("help")
    bot.add_cog(MainCog(bot))
    bot.run(logins[1])
except KeyboardInterrupt:
    bot.logout()
#/////////////////////////////////////////////////////////////////////////////#
