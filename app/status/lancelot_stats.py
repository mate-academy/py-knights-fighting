class LancelotStatus:
    def __init__(self, lancelot: object) -> None:
        self.lancelot = lancelot

    def lancelot_stats(self) -> dict:
        result_weapon = self.lancelot.lancelot_weapon()
        result_armour = self.lancelot.lancelot_armour()
        result_potion = self.lancelot.lancelot_potion()
        name = self.lancelot.name
        hp = self.lancelot.hp
        power = self.lancelot.power
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

        if result_weapon:
            for key, value in result_weapon.items():
                if key == "power":
                    power += value
        return {"name": name, "hp": hp,
                "power": power, "protection": protection}
