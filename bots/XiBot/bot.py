import discord
import discord.ext.commands as comms
import datetime
import time

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


class MainCog:
    def __init__(self, bot):
        self.bot = bot

    @comms.command(pass_context=True)
    async def google(self, ctx, searching, number):
        results = []
        embed=discord.Embed(title="Google search", description=f"The top {number} search results for {searching}")
        for j in search(searching, tld="com", num=number, stop=1, pause=2):
            results.append(j)
            print(j)
        '''
        for i in range(number):
            embed.add_field(name=f"{}")
        '''

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
                print(f"{ctx.message.author} has successfully changed status:")
                print(f"Status: {stat}, description: {desc}")
            else:
                await ctx.send(f"{stat} is an invalid parameter for $updateStatus")
        else:
            await ctx.send(f"{ctx.message.author.mention} you can't do this")

    @comms.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help 1/", description="This is the place where you get help", color=0x00ff01, timestamp=datetime.datetime.now())
        embed.add_field(name="command prefix", value="$", inline=False)
        embed.add_field(name="$updateStatus <status> <desc>", value="<status> can be online, offline, idle, dnd (do not disturb), or invisible. <desc> changes what the bot is playing.", inline=True)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await ctx.send(embed=embed)

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

bot = BotClient(command_prefix = '$', owner_id = 196664644113268736)
bot.remove_command('help')
bot.add_cog(MainCog(bot))
bot.run(token)
