class RedKnightStatus:

    def __init__(self, red_knight: object) -> None:
        self.red_knight = red_knight

    def red_knight_stats(self) -> dict:
        result_weapon = self.red_knight.red_knight_weapon()
        result_armour = self.red_knight.red_knight_armour()
        result_potion = self.red_knight.red_knight_potion()
        name = self.red_knight.name
        hp = self.red_knight.hp
        power = self.red_knight.power
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

        if self.red_knight.red_knight_weapon:
            for key, value in result_weapon.items():
                if key == "power":
                    power += value
        return {"name": name, "hp": hp,
                "power": power, "protection": protection}
