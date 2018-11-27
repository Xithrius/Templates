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
    async def updateStatus(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            check = True
            while check:
                x = list(str(f"{ctx.message.content}"))
                x[0:14] = ''
                for i in range(len(x)):
                    if x[i] == ',':
                        if x[i + 1] == ' ':
                            status = x[0:i]
                            desc = x[i + 2:]
                status = ''.join(str(y) for y in status)
                desc = ''.join(str(y) for y in desc)
                if status == 'online':
                    statusChange = discord.Status.online
                elif status == 'offline':
                    statusChange = discord.Status.offline
                elif status == 'idle':
                    statusChange = discord.Status.idle
                elif status == 'dnd':
                    statusChange = discord.Status.dnd
                elif status == 'invisible':
                    statusChange = discord.Status.invisible
                else:
                    ctx.send(f"{ctx.message.author.mention}! {status} isn't an acceptable option. For help, type $updateStatus help")
                    ctx.send("Options for status are `online`, `offline`, `idle`, `dnd (do not disturb)`, and `invisible`")
                    check = True
                await ctx.bot.change_presence(status=statusChange, activity=discord.Game(desc))
        else:
            await ctx.send(f"You don't have permission, {ctx.message.author.mention}")

    @comms.command()
    async def exit(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            await ctx.send('Cya nerds')
            await self.bot.logout()
        else:
            await ctx.send("You can't do that")

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
