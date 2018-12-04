import discord
import discord.ext.commands as comms

class MainCog:
    def __init__(self, bot):
        self.bot = bot

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

    @comms.command()
    async def sort(self, ctx):
        l = f"{ctx.message.content}".split()
        l = l[1:]
        wrongList = []
        l = sorted(l)
        wrongList = sorted(wrongList)
        if len(wrongList) > 0:
            await ctx.send(f"{ctx.message.author.mention} components `{wrongList}` cannot be in the list")
            await ctx.send("Here is your sorted list of components that aren't invalid:")
            await ctx.send(f"`{''.join(str(y) for y in l)}`")
        elif len(wrongList) == 0:
            await ctx.send(f"{ctx.message.author.mention} Here is your sorted list:")
            await ctx.send(f"`{l}`")

    @comms.command(pass_context=True)
    async def joined_at(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        await ctx.send(f"{member} joined on {member.joined_at}")

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
