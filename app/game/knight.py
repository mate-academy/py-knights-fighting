class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight.get("name")
        self.power = knight.get("power")
        self.hp = knight.get("hp")
        self.armour = knight.get("armour", [])
        self.weapon = knight.get("weapon")
        self.potion = knight.get("potion")
        self.protection = 0

        # ---------- Recalculate
        self.recalculate_stats()

    def recalculate_stats(self) -> None:

        # Armour
        for protection in self.armour:
            self.protection += protection.get("protection", 0)

        # Power
        self.power += self.weapon.get("power", 0)

        if self.potion is not None:

            effect = self.potion.get("effect", {})

            for stat in ["power", "protection", "hp"]:
                if stat in effect:
                    setattr(
                        self,
                        stat,
                        getattr(self, stat) + effect.get(stat, 0)
                    )
