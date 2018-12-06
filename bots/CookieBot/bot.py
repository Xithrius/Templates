import discord
import discord.ext.commands as comms

class MainCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_nou(self, ctx):
        if ctx.message.content == 'ur gay':
            await ctx.send(f"{ctx.message.author.mention} no u")

    @comms.command(pass_context=True)
    async def updateStatus(self, ctx, stat, desc=None):
        if await ctx.bot.is_owner(ctx.message.author):
            if stat == 'help':
                if desc == None:
                    await ctx.send("Format of command: $updateStatus <status>, <desc>")
                    await ctx.send("Options for status are `online`, `offline`, `idle`, `dnd (do not disturb)`, and `invisible`")
                    await ctx.send("Anything is allowed in the desc")
            elif stat in ['online', 'offline', 'idle', 'dnd', 'invisible']:
                await ctx.bot.change_presence(status=stat, activity=discord.Game(desc))
            else:
                await ctx.send(f"{stat} is an invalid parameter for $updateStatus")
        else:
            await ctx.send(f"{ctx.message.author.mention} you can't do this")

    @comms.group()
    async def cookies(self, ctx):
        if ctx.invoked_subcommand is None:
            await bot.send(f"{ctx.message.author.mention} invalid sub command passed")

    @cookies.command()
    async def help(self, ctx):
        pass

    @comms.command()
    async def exit(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            await ctx.send('Goodbye')
            await self.bot.logout()
        else:
            await ctx.send(f"{ctx.message.author.mention} You can't make me leave")

class BotClient(comms.Bot):
    async def on_ready(self):
        print(f"logging in as {bot.user}")
        print(f"{bot.user} ID: {bot.user.id}")
        print('Awaiting...')
        print('')

try:
    with open('login.txt', 'r') as f:
        token = f.read().strip()

except FileNotFoundError:
    with open('login.txt', 'w') as f:
        token = input('token: ')

        f.write(token)

bot = BotClient(command_prefix = '%', owner_id = 196664644113268736)

bot.add_cog(MainCog(bot))
#bot.add_cog(Events(bot))
bot.run(token)
