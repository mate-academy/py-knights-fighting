class Knight:
    def __init__(self, knights_config: dict) -> None:
        self.name = knights_config["name"]
        self.power = knights_config["power"]
        self.hp = knights_config["hp"]
        self.armour = knights_config["armour"]
        self.protection = 0
        self.weapon = knights_config["weapon"]
        self.weapon_used = False
        self.potion = knights_config["potion"]
        self.potion_used = False

    def use_protection(self) -> None:
        self.protection += sum(i["protection"] for i in self.armour)

    def use_weapon(self) -> None:
        if not self.weapon_used:
            self.power += self.weapon["power"]
            self.weapon_used = True

    def use_potion(self) -> None:
        if not self.potion_used and self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)
            self.potion_used = True
