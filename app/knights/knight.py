class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 weapon: int,
                 armour: list = None,
                 potion: dict = None):

        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion

    def knights_armour_equipping(self):
        armour_equipped = sum([armour_points.get("protection")
                               for armour_points in self.armour])
        return armour_equipped

    def knights_weapon_equipped(self):
        weapon_armour_equipped = self.weapon
        return weapon_armour_equipped

    def knights_potion_drinking(self):
        effects = self.potion.get("effect")
        power_boosted = 0
        hp_boosted = 0
        protection_boosted = 0
        if effects.get("power"):
            power_boosted += effects.get("power")
        if effects.get("hp"):
            hp_boosted += effects.get("hp")
        if effects.get("protection"):
            protection_boosted += effects.get("protection")

        return power_boosted, hp_boosted, protection_boosted
