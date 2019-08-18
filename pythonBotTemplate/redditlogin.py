import aiohttp
import json

# I'm just going to slap this here
# Attempting to connect to the Reddit API
f = {
"username": "",
"password": "",
"id": "",
"secret": ""
}
client_auth = aiohttp.BasicAuth(login=f['id'], password=f['secret'])
post_data = {"grant_type": "password", "username": f['username'], "password": f['password']}
headers = {"User-Agent": f"bot_name/v0.0.1 by {f['username']}"}
async with aiohttp.ClientSession(auth=client_auth, headers=headers) as session:
    async with session.post("https://www.reddit.com/api/v1/access_token", data=post_data) as r:
        if r.status == 200:
            js = await r.json()
            print('[ SUCCESS ]: REDDIT SERVICE AVAILABLE')
            services = {"Authorization": f"bearer {js['access_token']}", **headers}
        else:
            print(f'[ WARNING ]: REDDIT SERVICE NOT AVAILABLE: {r.status}')