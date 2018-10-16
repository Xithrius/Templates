import discord
from discord.ext import commands
import youtube_dl

try:
    with open('login.txt', 'r') as f:
        token = f.read().strip()
except FileNotFoundError:
    with open('login.txt', 'w') as f:
        token = input('Token: ')
        f.write(token)

client = commands.Bot(command_prefix = '%')

players = {}
queues = {}

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

@client.event
async def on_ready():
    print('Awaiting test bot...')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command()
async def exit(ctx):
    await client.send_message('bye')
    await client.logout()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    if len(queues) == 0:
        await client.say('Nothing in queue. audio will now play.')
    elif len(queues) == 1:
        await client.say('Audio will play after this one is finished')
    else:
        await client.say(f'Video will play after {len(queues)} others are done')


client.run(token)
