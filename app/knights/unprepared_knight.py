from app.knights.prepared_knight import PreparedKnight


class UnpreparedKnight:
    def __init__(self, knight: dict) -> None:
        self.name = knight.get("name")
        self.power = knight.get("power")
        self.hp = knight.get("hp")
        self.protection = 0
        self.armour = knight.get("armour")
        self.weapon = knight.get("weapon")
        self.potion = knight.get("potion")

    def battle_preparation(self) -> PreparedKnight:
        if self.armour:
            self.protection += sum(
                item.get("protection", 0) for item in self.armour
            )
            print(f"{self.name} equipped his armour")
        else:
            print(f"{self.name} will fight without armour")

        self.power += self.weapon.get("power", 0)
        print(f"{self.name} prepared his weapon")

        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            print(f"{self.name} activated all his potions")
        else:
            print(f"{self.name} needs no potion for fight")

        return PreparedKnight(
            name=self.name,
            power=self.power,
            hp=self.hp,
            protection=self.protection
        )
