from app.knights_equipment import Armor, Weapon, Potion


class Knight:
    def __init__(self,
                 knights_config: dict) -> None:
        self.name = knights_config["name"]
        self.power = knights_config["power"]
        self.hp = knights_config["hp"]
        self.armour = knights_config["armour"]
        self.weapon = knights_config["weapon"]
        self.potion = knights_config["potion"]
        self.protection = 0

    def __repr__(self) -> str:
        return f"{self.name}: {self.hp}"

    def apply_armor(self) -> None:
        self.armour = [Armor(arm_prt["part"],
                             arm_prt["protection"]) for arm_prt in self.armour]
        for item in self.armour:
            self.protection += item.protection

    def apply_weapon(self) -> None:
        self.weapon = Weapon(self.weapon["name"], self.weapon["power"])
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.potion = Potion(self.potion["name"], self.potion["effect"])
            self.power += self.potion.effect.get("power", 0)
            self.hp += self.potion.effect.get("hp", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def battle_preparations(self) -> None:
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()
