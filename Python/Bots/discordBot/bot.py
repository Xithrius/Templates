import discord


import discord.ext.commands as comms

class MainCog:
    def __init__(self, bot):
        self.bot = bot

    @comms.command()
    async def hello(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            await ctx.send('Hi')
        else:
            await ctx.send('Hello')

    @comms.command()
    async def exit(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            await ctx.send('bi')
            await self.bot.logout()
        else:
            await ctx.send("NOOOOOOOOOOOOOOOOO")

    @comms.command()
    async def hippity(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            await ctx.send('hippity hoppity u own my property')
        else:
            await ctx.send('hippity')
            await asyncio.sleep(1)
            await ctx.send('hoppity')
            await asyncio.sleep(1)
            await ctx.send('get off')
            await asyncio.sleep(1)
            await ctx.send('this')
            await asyncio.sleep(1)
            await ctx.send('PROPERTY!!!')


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
