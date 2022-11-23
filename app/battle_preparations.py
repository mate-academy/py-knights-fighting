from __future__ import annotations


class Knights:
    def __init__(self, info: dict) -> None:
        self.info = info
        self.name = info["name"]
        self.hp = self.info["hp"]
        self.power = self.info["power"] + self.info["weapon"]["power"]
        self.protection = 0
        self.potion_effect()
        self.protection_total()

    def potion_effect(self) -> None:
        if self.info["potion"] is not None:
            for effect in self.info["potion"]["effect"]:
                if effect == "hp":
                    self.hp += self.info["potion"]["effect"]["hp"]

                if effect == "power":
                    self.power += self.info["potion"]["effect"]["power"]

                if effect == "protection":
                    self.protection += \
                        self.info["potion"]["effect"]["protection"]

    def protection_total(self) -> int:
        if len(self.info["armour"]) > 0:
            for armour in self.info["armour"]:
                self.protection += armour["protection"]
        return self.protection

    def hp_check(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def holding_a_battle(self, other: Knights) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        self.hp_check()
        other.hp_check()
