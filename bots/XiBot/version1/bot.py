import discord
import discord.ext.commands as comms

class MainCog:
    def __init__(self, bot):
        self.bot = bot

    @comms.group()
    async def updateStatus(self, ctx):
        if ctx.invoked_subcommand is None:
            pass
    @updateStatus.command(pass_context=True)
    async def online(self, ctx, ):


    @updateStatus.command()
    async def help(self, ctx):
        await ctx.send("Format of command: $updateStatus <status>, <desc>")
        await ctx.send("Options for status are `online`, `offline`, `idle`, `dnd (do not disturb)`, and `invisible`")
        await ctx.send("Anything is allowed in the desc")

    @comms.command(pass_context=True)
    async def joined_at(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        await ctx.send('{0} joined on {0.joined_at}'.format(member))

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
