class Knight:

    def __init__(
        self,
        data: dict,
    ) -> None:

        self.name = data["name"]
        self.base_power = data["power"]
        self.base_hp = data["hp"]

        self.protection = sum(item["protection"] for item in data["armour"])
        self.power = self.base_power + data["weapon"]["power"]
        self.hp = self.base_hp

        potion = data.get("potion")

        if potion:
            self.apply_potion(potion)

    def apply_potion(self, potion: dict) -> None:

        effect = potion.get("effect")
        if effect:
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:

        self.hp -= opponent_power - self.protection

        if self.hp <= 0:
            self.hp = 0
