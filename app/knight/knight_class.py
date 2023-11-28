class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def apply_armor(self, knights: dict) -> None:
        for knight in knights:
            if knights[knight]["name"] == self.name:
                for item in knights[knight]["armour"]:
                    self.protection += item["protection"]

    def equip_weapon(self, knights: dict) -> None:
        for knight in knights:
            if knights[knight]["name"] == self.name:
                self.power += knights[knight]["weapon"]["power"]

    def use_potion(self, knights: dict) -> None:
        potion = self.extract_potion(knights)
        for key, value in potion.items():
            if value is not None:
                if "power" in value["effect"]:
                    self.power += value["effect"]["power"]

                if "protection" in value["effect"]:
                    self.protection += value["effect"]["protection"]

                if "hp" in value["effect"]:
                    self.hp += value["effect"]["hp"]

    def extract_potion(self, knights: dict) -> dict:
        return {
            knights[knight]["name"]: knights[knight]["potion"]
            for knight in knights
            if knights[knight]["name"] == self.name
        }

    def attack(self, opponent_hp: int, opponent_protection: int) -> int:
        opponent_hp -= self.power - opponent_protection
        return opponent_hp
