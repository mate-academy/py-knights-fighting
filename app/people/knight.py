from typing import Union


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: Union[None, dict]) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.battle_stats = {
            "hp": hp,
            "power": power,
            "protection": 0
        }
        self.update_battle_stats()

    def update_battle_stats(self) -> None:
        self.battle_stats = {
            "hp": self.hp,
            "power": self.power,
            "protection": 0
        }
        for piece in self.armour:
            protection = piece.get("protection", 0)
            self.battle_stats["protection"] += protection

        weapon_power = self.weapon.get("power", 0)
        self.battle_stats["power"] += weapon_power

        if self.potion:
            potion_effect = self.potion.get("effect", {})
            potion_power = potion_effect.get("power", 0)
            potion_hp = potion_effect.get("hp", 0)
            potion_protection = potion_effect.get("protection", 0)

            self.battle_stats["power"] += potion_power
            self.battle_stats["hp"] += potion_hp
            self.battle_stats["protection"] += potion_protection
