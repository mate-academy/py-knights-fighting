class MordredStatus:
    def __init__(self, mordred: object) -> None:
        self.mordred = mordred

    def mordred_stats(self) -> dict:
        result_weapon = self.mordred.mordred_weapon()
        result_armour = self.mordred.mordred_armour()
        result_potion = self.mordred.mordred_potion()
        name = self.mordred.name
        hp = self.mordred.hp
        power = self.mordred.power
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

        if self.mordred.mordred_weapon:
            for key, value in result_weapon.items():
                if key == "power":
                    power += value
        return {"name": name, "hp": hp,
                "power": power, "protection": protection}
