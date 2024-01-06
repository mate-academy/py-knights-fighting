class ArthurStatus:

    def __init__(self, arthur: object) -> None:
        self.arthur = arthur

    def arthur_stats(self) -> dict:
        result_weapon = self.arthur.arthur_weapon()
        result_armour = self.arthur.arthur_armour()
        result_potion = self.arthur.arthur_potion()
        name = self.arthur.name
        hp = self.arthur.hp
        power = self.arthur.power
        protection = 0
        if result_potion is None:
            hp += 0
            power += 0
            protection += 0
        else:
            for key, value in result_potion.items():
                if key == "hp":
                    if value > 0:
                        hp += value
                    else:
                        hp -= abs(value)
                elif key == "power":
                    if value > 0:
                        power += value
                    else:
                        power -= abs(value)
                else:
                    if value > 0:
                        protection += value
                    else:
                        protection -= abs(value)

        if result_armour is None:
            protection += 0
        else:
            for row in result_armour:
                protection += row["protection"]

        if self.arthur.arthur_weapon:
            for key, value in result_weapon.items():
                if key == "power":
                    power += value
        return {"name": name, "hp": hp,
                "power": power, "protection": protection}
