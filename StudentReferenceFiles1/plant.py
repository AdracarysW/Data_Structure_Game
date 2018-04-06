from organism import Organism

class Plant(Organism):

    cost = 35

    def __init__(self):
        super().__init__()
        self.powerup = 0
        self.dmg = 0
        self.hp = 0

    def attack(self, nonplant):
        nonplant.take_damage(self.dmg)

    def apply_powerup(self, card):
         self.powerup = card.power + self.powerup

    def weaken_powerup(self):
        self.powerup = self.powerup / 2
