import discord
from discord.ext import commands as comms
import os
import json
import platform
import sys


# Different paths for different operating systems
def pathing(object):
    if platform.system() == "Windows":
        return f"{os.path.dirname(os.path.realpath(__file__))}\\{object}"
    elif platform.system() == "Linux":
        return f"{os.path.dirname(os.path.realpath(__file__))}/{object}"


class MainCog():
    def __init__(self, bot):
        self.bot = bot

    @comms.command()
    async def exit(self, ctx):
        if await ctx.bot.is_owner(ctx.author):
            print("Exiting...")
            await self.bot.logout()
        else:
            await ctx.send(f"{ctx.author.mention} you cannot do this")


def initErrorCheck():
    try:
        with open(pathing('login.json'), "r") as f:
            login = json.load(f)
            return [login["discord"]["owner_id"], login["discord"]["bot_token"]]
    except FileNotFoundError:
        with open(pathing('login.json'), "w") as f:
            errorPrompt("")
    except IndexError:
        errorMessage("The file login.json has been modified manually and cannot be read.", sys.exc_info())


def errorPrompt(string, type=None):
    if type != None:
        x = f"#{'/' * len(string)}#"
        print(f"{x}\n{type}:\n{string}\n{x}")
    else:
        x = f"#{'/' * len(string)}#"
        print(f"{x}\n{string}\n{x}")


class BotClient(comms.Bot):
    async def on_ready(self):
        print(f"Logging in as {bot.user}")
        print(f"{bot.user} ID: {bot.user.id}")
        print("Awaiting...")


logins = initErrorCheck()
bot = BotClient(command_prefix = "$", owner_id = logins[0])
bot.remove_command("help")
bot.add_cog(MainCog(bot))
bot.run(logins[1])
