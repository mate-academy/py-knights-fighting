class Knight:
    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info.get("name")
        self.power = knight_info.get("power")
        self.hp = knight_info.get("hp")
        self.protection = 0
        self.arsenal = [knight_info.get("armour"),
                        knight_info.get("weapon"),
                        knight_info.get("potion")]

    def get_amount_of_protection(self) -> int:
        return sum(part.get("protection")
                   for part in self.arsenal[0])

    def get_weapon_power(self) -> int:
        return self.arsenal[1].get("power")

    def get_potion_effects(self) -> dict:
        result = {
            "hp": 0,
            "power": 0,
            "protection": 0
        }
        if self.arsenal[2] is not None:
            if self.arsenal[2].get("effect").get("hp") is not None:
                result["hp"] = self.arsenal[2].get("effect").get("hp")
            if self.arsenal[2].get("effect").get("power") is not None:
                result["power"] = self.arsenal[2].get("effect").get("power")
            if self.arsenal[2].get("effect").get("protection") is not None:
                result["protection"] = (self.arsenal[2]
                                        .get("effect")
                                        .get("protection"))
        return result

    def prepare_to_battle(self) -> None:
        self.protection += (self.get_amount_of_protection()
                            + self.get_potion_effects().get("protection"))
        self.power += (self.get_weapon_power()
                       + self.get_potion_effects().get("power"))
        self.hp += self.get_potion_effects().get("hp")

    def update_hp(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def print_info(self) -> None:
        print(f"Knight: {self.name}, "
              f"HP: {self.hp}, Power: {self.power}, "
              f"Weapon: {self.get_weapon_power()}, "
              f"Protection: {self.protection}, "
              f"Effects: {self.get_potion_effects()}")
