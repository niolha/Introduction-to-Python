import random


class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self._health = 100
        self.strength = 1
        self.skill = 1
        self.mind = 1

    @property
    def health(self):
        return self._health

    def healing(self):
        self._health = min(self._health + 10, 100)

    @staticmethod
    def calculate_basic_skill(basic_skill):
        return min(basic_skill + 1, 10)

    def __str__(self):
        return f"Name: {self.name.title()}, Clan: {self.clan.title()}, " \
               f"Health: {self._health}, Strength: {self.strength}, " \
               f"Skill: {self.skill}, Mind: {self.mind}"


class Mage(Unit):
    def __init__(self, name, clan):
        super(Mage, self).__init__(name, clan, )
        magics = ["air", "flame", "aqua"]
        self.magic = random.choice(magics)

    def increase_basic_skill(self):
        self.mind = self.calculate_basic_skill(self.mind)

    def __str__(self):
        line = super().__str__()
        return f"Type: Mage, {line}, Magic: {self.magic.title()}"


class Archer(Unit):
    def __init__(self, name, clan):
        super(Archer, self).__init__(name, clan)
        bows = ["bow", "crossbow", "sling"]
        self.bow = random.choice(bows)

    def increase_basic_skill(self):
        self.skill = self.calculate_basic_skill(self.skill)

    def __str__(self):
        line = super().__str__()
        return f"Type: Archer, {line}, Bow: {self.bow.title()}"


class Knight(Unit):
    def __init__(self, name, clan):
        super(Knight, self).__init__(name, clan)
        weapons = ["sword", "ax", "peak"]
        self.weapon = random.choice(weapons)

    def increase_basic_skill(self):
        self.strength = self.calculate_basic_skill(self.strength)

    def __str__(self):
        line = super().__str__()
        return f"Type: Knight, {line}, Weapon: {self.weapon.title()}"


mage = Mage("woland", "demons")
print(mage)
mage.increase_basic_skill()
mage.increase_basic_skill()
mage.healing()
print(mage)
archer = Archer("legolas", "grey elves")
print(archer)
archer.increase_basic_skill()
print(archer)
knight = Knight("don quijot", "lions")
print(knight)
knight.increase_basic_skill()
print(knight)
