class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def stats(self) -> dict:
        hp = self.hp
        power = self.power + self.weapon["power"]
        protection = 0
        for prot in self.armour:
            protection += prot["protection"]

        if self.potion is not None:
            if "hp" in self.potion["effect"]:
                hp += self.potion["effect"]["hp"]
            if "power" in self.potion["effect"]:
                power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                protection += self.potion["effect"]["protection"]

        return {
            "hp": hp,
            "power": power,
            "protection": protection
        }

    def fight(self, enemy: "Knight") -> dict:
        first_hp = self.stats()["hp"]
        second_hp = enemy.stats()["hp"]

        first_power = self.stats()["power"]
        second_power = enemy.stats()["power"]

        first_protection = self.stats()["protection"]
        second_protection = enemy.stats()["protection"]

        first_hp -= second_power - first_protection
        second_hp -= first_power - second_protection

        if first_hp <= 0:
            first_hp = 0

        if second_hp <= 0:
            second_hp = 0

        self.hp = first_hp
        enemy.hp = second_hp
