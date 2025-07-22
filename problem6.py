import copy


class NPC:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def clone(self):
        return copy.deepcopy(self)


NPC1 = NPC("test1", "test2")
NPC2 = NPC1.clone()
print(NPC1 == NPC2)
