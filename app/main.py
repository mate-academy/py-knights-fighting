class Knights:
    def __init__(self, configurations):
        self.name = configurations['name']
        self.hp = configurations["hp"]
        self.power = configurations["power"]
        self.apply_arm(configurations["armour"])
        self.apply_weapon(configurations["weapon"])
        if configurations["potion"]:
            self.apply_potions(configurations["potion"])

    def apply_arm(self, armor):
        for health in armor:
            self.hp += health["protection"]

    def apply_weapon(self, weapon):
        self.power += weapon["power"]

    def apply_potions(self, potion):
        pot_effect = potion["effect"]
        for item in pot_effect:
            if item == "hp":
                self.hp += pot_effect["hp"]
            elif item == "protection":
                self.hp += pot_effect["protection"]
            else:
                self.power += pot_effect["power"]

    def damage(self, amount_of_damage):
        if amount_of_damage > self.hp:
            self.hp = 0
        else:
            self.hp -= amount_of_damage

    def battle(knights_config):
        knights = []
        for knight in knights_config.values():
            knights.append(Knights(knight))
        knights[0].damage(knights[2].power)
        knights[2].damage(knights[0].power)
        knights[1].damage(knights[3].power)
        knights[3].damage(knights[1].power)
        return {knight.name: knight.hp for knight in knights}
