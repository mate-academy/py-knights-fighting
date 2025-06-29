from __future__ import annotations


class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.knight_config = knight_config
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.protection = 0

    def prepare(self) -> None:
        for armour in self.knight_config.get("armour", []):
            self.protection += armour.get("protection", 0)

        self.power += self.knight_config["weapon"]["power"]

        if self.knight_config.get("potion"):
            potion = self.knight_config.get("potion", {}).get("effect", {})
            self.hp += potion.get("hp", 0)
            self.power += potion.get("power", 0)
            self.protection += potion.get("protection", 0)

    def fight(self, other: Knight) -> None:
        if isinstance(other, Knight):
            self.hp -= other.power - self.protection
            other.hp -= self.power - other.protection

            self.hp = max(self.hp, 0)
            other.hp = max(other.hp, 0)
        else:
            raise TypeError("Knight can fight only other knight.")
