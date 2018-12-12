import json
import os



dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/gungeoneers.json', 'r') as f:
    gungeoneers = json.load(f)
print(gungeoneers["The Convict"]["Starting Weapons"][0:])



@comms.command(pass_context=True)
async def etg(self, ctx, searchType, name):
    if searchType in ['gungeoneers', 'items', 'guns', 'bosses', 'CotG']:
        with open(f"pathing() + /{searchType}.json", 'r') as f:
            gungeoneer = json.load(f)
        embed=discord.Embed(title=f"{gungeoneer}", description="This is the place where you get help", color=300000, timestamp=datetime.datetime.now())
    else:
        ctx.send(f"{ctx.message.author.mention} {searchType} only Gungeoneers, Items, Guns, Bosses, and the Cult of the Gundead exist")
