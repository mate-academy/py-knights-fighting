# BATTLE PREPARATIONS:

class CreateKnight:
    def __init__(self, knight: dict) -> None:
        self.name = knight.get("name")
        self.protection = 0
        self.power = knight.get("power")
        self.hp = knight.get("hp")
        self.arsenal = [
            knight.get("armour"),
            knight.get("weapon"),
            knight.get("potion")
        ]

    def potion_effects(self) -> dict:
        effects = {
            "power": 0,
            "protection": 0,
            "hp": 0
        }

        if self.arsenal[2]:
            if self.arsenal[2].get("effect").get("power"):
                effects["power"] += self.arsenal[2].get("effect").get("power")

            if self.arsenal[2].get("effect").get("protection"):
                effects["protection"] += (self.arsenal[2]
                                          .get("effect")
                                          .get("protection"))

            if self.arsenal[2].get("effect").get("hp"):
                effects["hp"] += self.arsenal[2].get("effect").get("hp")
        return effects

    def get_protection(self) -> int:
        return sum(part.get("protection") for part in self.arsenal[0])

    def get_power(self) -> int:
        return self.arsenal[1].get("power")

    def prepare_for_battle(self) -> None:
        self.protection += (self.get_protection()
                            + self.potion_effects()["protection"])
        self.power += self.get_power() + self.potion_effects()["power"]
        self.hp += self.potion_effects()["hp"]

    def update_hp(self) -> None:
        if self.hp <= 0:
            self.hp = 0
