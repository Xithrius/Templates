import json
import pickle

class Structure:
    cost = -1
    def cps(self):
        raise NotImplementedError()

    def name(self):
        raise NotImplementedError()

class MilkMan(Structure):
    cost = 10
    def cps(self):
        return 10

    def name(self):
        return 'Milk Man'


class SaveGame:
    def __init__(self, cookies, buildings):
        self.cookies = cookies
        self.buildings = buildings

    def tick(self):
        for b in self.buildings:
            num, am = b

            self.cookies += num * am

    def save(self, fp):
        with open(fp, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(fp):
        with open(fp, 'rb') as f:
            return pickle.load(f)


### JSON
# state = {'cookies': 0, 'buildings': [(0, 0), (1, 0), (2, 0)]}
#
# with open('saveGame.json', 'w') as f:
#     json.dump(state, f)
#
# with open('saveGame.json', 'r') as f:
#     newState = json.load(f)
#
# print(newState, state)


### PICKLE
save = SaveGame(0, [(4, 1), (1, 2), (2, 3)])
print(save.cookies)
save.tick()
print(save.cookies)

save.save('saveGame2.pkl')

newSave = SaveGame.load('saveGame2.pkl')

newSave.tick()

print(save.cookies, newSave.cookies)
