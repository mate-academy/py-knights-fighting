from dataclasses import dataclass


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: list[dict] | None
    weapon: dict
    potion: dict | None

    def calculate_total_power(self) -> dict:
        final_protection = 0
        final_hp = self.hp
        final_dmg = self.weapon["power"] + self.power

        if self.armour:
            for armor in self.armour:
                final_protection += armor["protection"]

        if self.potion:
            if "power" in self.potion["effect"]:
                final_dmg += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                final_protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                final_hp += self.potion["effect"]["hp"]

        result = {
            "name": self.name,
            "power": final_dmg,
            "hp": final_hp,
            "protection": final_protection
        }

        return result
