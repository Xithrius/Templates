import json

with open('D:/github_repositories/CODING/bots/XiBot/ETGinfo/Gungeoneers.json', 'r') as f:
    gungeoneers = json.load(f)
print(gungeoneers["The Convict"]["Starting Weapons"])
