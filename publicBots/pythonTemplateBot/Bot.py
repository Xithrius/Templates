import discord
from discord.ext import commands as comms
import os


def pathing():
    return os.path.dirname(os.path.realpath(__file__))
    # Directory (folder) path

class MainCog():
    def __init__(self, bot):
        self.bot = bot

# commands here

    @comms.command()
    async def exit(self, ctx):
        if await ctx.bot.is_owner(ctx.author):
            print("Exiting...")
            await self.bot.logout()
        else:
            await ctx.send(f"{ctx.author.mention} you can't do this")

class BotClient(comms.Bot):
    async def on_ready(self):
        print(f"logging in as {bot.user}")
        print(f"{bot.user} ID: {bot.user.id}")
        print('Awaiting...')
try:
    with open(f'{pathing}/login.txt', 'r') as f:
        token = f.read().strip()
except FileNotFoundError:
    with open(f'{pathing}/login.txt', 'w') as f:
        token = input('token: ')
        f.write(token)
bot = BotClient(command_prefix = '$', owner_id = '''OWNER ID''')
# "bot.remove_command('help')" To remove built in commands
bot.add_cog(MainCog(bot))
bot.run(token)
