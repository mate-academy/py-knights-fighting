from typing import Any

from app.preparations.hp import Hp
from app.preparations.protection import Protection
from app.preparations.power import Power


class Knight:
    def __init__(self, config: dict) -> None:
        self.knight_config = config

    def preparations(self) -> dict[str, Any]:
        hp = Hp(self.knight_config["hp"])

        protection = Protection()
        for armour in self.knight_config["armour"]:
            protection.add_protection(armour["protection"])

        power = Power(self.knight_config["power"])
        power.add_power(self.knight_config["weapon"]["power"])

        if self.knight_config["potion"] is not None:
            if "power" in self.knight_config["potion"]["effect"]:
                power.add_power(
                    self.knight_config["potion"]["effect"]["power"])

            if "protection" in self.knight_config["potion"]["effect"]:
                protection.add_protection(
                    self.knight_config["potion"]["effect"]["protection"])

            if "hp" in self.knight_config["potion"]["effect"]:
                hp.add_hp(
                    self.knight_config["potion"]["effect"]["hp"])

        return {
            "name": self.knight_config["name"],
            "hp": hp.hp,
            "protection": protection.protection,
            "power": power.power,
        }
