import discord
import discord.ext.commands as comms

import stripCommand

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
    async def poke(self, ctx, member: discord.Member):
        await ctx.send_message(member, 'boop')
    #@comms.command(pass_context=True)
    #async def poke(self, ctx, message):
    #    await ctx.bot.send_message(ctx.message.author, 'boop')

    @comms.command()
    async def updateStatus(self, ctx):
        if await ctx.bot.is_owner(ctx.message.author):
            update = stripCommand.main(list(f"{ctx.message.content}"))
            if update[0] == 'Help':
                await ctx.send("Format of command: $updateStatus <status>, <desc>")
                await ctx.send("Options for status are `online`, `offline`, `idle`, `dnd (do not disturb)`, and `invisible`")
                await ctx.send("Anything is allowed in the desc")
            elif update[0] == 'online':
                await ctx.bot.change_presence(status=discord.Status.online, activity=discord.Game(update[1]))
            elif update[0] == 'offline':
                await ctx.bot.change_presence(status=discord.Status.offline, activity=discord.Game(update[1]))
            elif update[0] == 'idle':
                await ctx.bot.change_presence(status=discord.Status.idle, activity=discord.Game(update[1]))
            elif update[0] == 'dnd':
                await ctx.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(update[1]))
            elif update[0] == 'invisible':
                await ctx.bot.change_presence(status=discord.Status.invisible, activity=discord.Game(update[1]))
            elif discord.ext.commands.errors.CommandInvokeError():
                await ctx.send(f"{ctx.message.author.mention}! {ctx.message.content} isn't an acceptable command. For help, type $updateStatus help")
            if update[0] != 'Help':
                print(f"User {ctx.message.author}: Status successfully changed to {update[0]}, desc changed to {update[1]}")
            else:
                print(f"User {ctx.message.author}: successfully asked for help")
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
