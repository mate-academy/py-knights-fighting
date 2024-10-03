class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: None | dict) -> None:
        self.name = name

        # Расчет силы с учетом оружия и зелья
        self.power = int(power) + int(weapon["power"])
        if (isinstance(potion, dict) and "effect" in potion
                and "power" in potion["effect"]):
            self.power += potion["effect"]["power"]

        # Расчет брони с учетом доспехов и зелья
        self.armour = 0
        for armour_element in armour:
            self.armour += armour_element["protection"]
        if (isinstance(potion, dict) and "effect" in potion
                and "protection" in potion["effect"]):
            self.armour += potion["effect"]["protection"]

        # Расчет очков здоровья с учетом зелья
        self.hp = hp
        if (isinstance(potion, dict) and "effect" in potion
                and "hp" in potion["effect"]):
            self.hp += potion["effect"]["hp"]

        self.greetings()

    def greetings(self) -> None:
        print(f"Welcome knight {self.name} to our tournament.\n",
              f"{self.name} characteristics: \n",
              f"\t\t hp - {self.hp}\n",
              f"\t\t power - {self.power}\n",
              f"\t\t armour - {self.armour}\n",)
