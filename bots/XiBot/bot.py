import discord
import discord.ext.commands as comms

class MainCog:
    def __init__(self, bot):
        self.bot = bot

    @comms.command()
    async def hello(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            await ctx.send('Greetings, Lord Farquad')
        else:
            await ctx.send(f"Hello {ctx.message.author.mention}")

    @comms.command()
    async def hippity(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            await ctx.send(f'{ctx.message.author.mention} Hippity hoppity I am your property')
        else:
            await ctx.send(f"{ctx.message.author.mention} I'm not your property")

    @comms.command()
    async def change_presence(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            x = list(str(f"{ctx.message.content}"))
            x[0:10] = ''
            str1 = ''.join(str(i) for i in x)
            await ctx.bot.change_presence(status=discord.Status.online, activity=discord.Game(str1))
        else:
            await ctx.send(f"You don't have permission, {ctx.message.author.mention}")

    @comms.command()
    async def updateStatus(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            x = list(str(f"{ctx.message.content}"))
            x[0:13] = ''
            # $updateStatus offline, none
            if x[0:7] == list('offline'):
                ctx.bot.change_presence(status=discord.Status.offline, activity=None)


    @comms.command()
    async def exit(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            await ctx.send('bi')
            await self.bot.logout()
        else:
            await ctx.send("NOOOOOOOOOOOOOOOOO")

    @comms.command()
    async def allHail(self, ctx):
        await ctx.send(f"All hail {ctx.message.member.role}")


class BotClient(comms.Bot):
    async def on_ready(self):
        print('Awaiting...')


try:
    with open('login.txt', 'r') as f:
        token = f.read().strip()

except FileNotFoundError:
    with open('login.txt', 'w') as f:
        token = input('token: ')

        f.write(token)

bot = BotClient(command_prefix = '$', owner_id = 196664644113268736)

bot.add_cog(MainCog(bot))
bot.run(token)
