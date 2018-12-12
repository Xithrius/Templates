import json
import os



dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/gungeoneers.json', 'r') as f:
    gungeoneers = json.load(f)
print(gungeoneers["The Convict"]["Starting Weapons"][0])
