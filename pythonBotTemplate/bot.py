#-----------------------------------------------------------------------------#
# Libraries
#-----------------------------------------------------------------------------
from discord.ext import commands as comms
import discord
import sys
import os
import platform
#/////////////////////////////////////////////////////////////////////////////#


#=============================================================================#
#=============================================================================#
# Essential functions
#=============================================================================#
#=============================================================================#


#-----------------------------------------------------------------------------#
# Different paths for different operating systems
#####################
# os, platform
#-----------------------------------------------------------------------------
def pathing(object):
    if platform.system() == "Windows":
        return f"{os.path.dirname(os.path.realpath(__file__))}\\{object}"
    elif platform.system() == "Linux":
        return f"{os.path.dirname(os.path.realpath(__file__))}/{object}"
    else:
        errorPrompt("Platform is not supported. Contact my creator.")
#/////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------#
# Custom error printing to the console
######################################
# Python built in libraries
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
# Custom input looping from console
###################################
# Python built in libraries
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


#=============================================================================#
#=============================================================================#
# Cogs
#=============================================================================#
#=============================================================================#


#-----------------------------------------------------------------------------#
# Main cog for commands and events
#####################
# discord.ext.commands as comms
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
# Checking to see if credentials exist to start bot
###################################################
# json
#-----------------------------------------------------------------------------
def initFileCheck():
    try:
        with open(pathing('credentials.json'), "r") as f:
            login = json.load(f)
            return [login["discord"]["owner_id"], login["discord"]["bot_token"]]
    except FileNotFoundError:
        errorMessage("The file login.json cannot be found.", sys.exc_info())
        with open(pathing('credentials.json'), "r+") as f:
            owner_id = input("Input discord user owner for owner_id: ")
            bot_token = input("Input discord bot token for bot_token: ")
            tokens = {
            "discord": [owner_id, bot_token]
            }
            json.dump(logins, f)
    except IndexError:
        errorMessage("The file credentials.json has been modified and cannot be read.", sys.exc_info())
#/////////////////////////////////////////////////////////////////////////////#


#=============================================================================#
#=============================================================================#
# Running everything
#=============================================================================#
#=============================================================================#


#-----------------------------------------------------------------------------#
# Turning on the bot with some error checking
###################################
# discord.ext.commands as comms
#-----------------------------------------------------------------------------
class BotClient(comms.Bot):
    async def on_ready(self):
        print(f"Logging in as {bot.user}")
        print(f"{bot.user} ID: {bot.user.id}")
        print("Awaiting...")

logins = initErrorCheck()
try:
    bot = BotClient(command_prefix = "$", owner_id = logins[0])
    bot.remove_command("help")
    bot.add_cog(MainCog(bot))
    bot.run(logins[1])
except KeyboardInterrupt:
    bot.logout()
#/////////////////////////////////////////////////////////////////////////////#
