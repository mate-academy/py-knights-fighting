class PlayerStatus:
    def __init__(self, player: object) -> None:
        self.player = player

    def player_stats(self) -> dict:
        result_weapon = getattr(self.player, "weapon")
        result_armour = getattr(self.player, "armour")
        result_potion = getattr(self.player, "potion")
        name = getattr(self.player, "name")
        hp = getattr(self.player, "hp")
        power = getattr(self.player, "power")
        protection = getattr(self.player, "protection")
        hp += 0
        power += 0
        protection += 0

        if result_potion is not None:
            for key, value in result_potion["effect"].items():
                if key == "hp":
                    hp += value
                elif key == "power":
                    power += value
                else:
                    protection += value

        if result_armour is not None:
            protection += sum(row["protection"] for row in result_armour)

        if result_weapon:
            power += result_weapon.get("power", 0)

        return {"name": name, "hp": hp,
                "power": power, "protection": protection}
