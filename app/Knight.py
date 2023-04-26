class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 protection: int
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @staticmethod
    def prepare_to_battle(knights_dict: dict) -> list:
        knights_list = []

        for knight in knights_dict.values():
            name = knight.get("name")
            power = knight.get("power") + knight.get("weapon").get("power")
            hp = knight.get("hp")
            protection = 0
            for armour in knight.get("armour"):
                protection += armour.get("protection")
            if knight.get("potion"):
                effect = knight.get("potion").get("effect")
                if "protection" in knight.get("potion").get("effect"):
                    protection += effect.get("protection")
                if "hp" in knight.get("potion").get("effect"):
                    hp += effect.get("hp")
                if "power" in knight.get("potion").get("effect"):
                    power += effect.get("power")

            knights_list.append(Knight(name, power, hp, protection))
        return knights_list
