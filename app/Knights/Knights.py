class KnightBasic:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 weapon: dict,
                 armour: list[dict] = None,
                 potion: dict = None
                 ) -> None:

        # basic attributes
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.weapon = weapon

        # additional attributes
        self.armour = armour
        self.potion = potion

    def battle_preparing(self):
        # take weapon to arms
        self.power += self.weapon["power"]

        # wear armour if you have one
        if self.armour:
            for equip in self.armour:
                self.protection += equip["protection"]

        # drink potion if you have one
        if self.potion:
            for effect in self.potion.get("effect"):
                if "power" == effect:
                    self.power += self.potion.get("effect").get(effect)
                if "hp" == effect:
                    self.hp += self.potion.get("effect").get(effect)
                if "protection" == effect:
                    self.protection += self.potion.get("effect").get(effect)
