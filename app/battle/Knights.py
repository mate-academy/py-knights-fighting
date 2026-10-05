from app.battle.types import KnightConfig


class Knight:
    def __init__(self, config: KnightConfig) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = Knight.calculate_power(config)
        self.protection = Knight.calculate_protection(config["armour"])
        self.calculate_potion_for_knight(config)

    def fight_with(self, other_knight: Knight) -> None :
        self.hp -= other_knight.power - self.protection
        other_knight.hp -= self.power - other_knight.protection

        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0

        if other_knight.hp <= 0:
            other_knight.hp = 0

    def calculate_potion_for_knight(self, config_item: KnightConfig) -> None:
        if config_item["potion"] is None:
            return

        effect = config_item["potion"]["effect"]

        if "power" in effect:
            self.power += effect["power"]

        if "protection" in effect:
            self.protection += effect["protection"]

        if "hp" in effect:
            self.hp += effect["hp"]

    @staticmethod
    def calculate_power(config: KnightConfig) -> int:
        return config["power"] + config["weapon"]["power"]

    @staticmethod
    def calculate_protection(knight_armour: list) -> int:
        armour = 0

        for item in knight_armour:
            armour += item["protection"]

        return armour
