from dataclasses import dataclass, field
from typing import List, Optional, Dict

from app.models.armour import Armour
from app.models.weapon import Weapon
from app.models.potion import Potion


@dataclass
class Knight:
    name: str
    base_hp: int
    base_power: int
    armour: List[Armour] = field(default_factory=list)
    weapon: Optional[Weapon] = None
    potion: Optional[Potion] = None

    @classmethod
    def from_config(cls, config: Dict) -> "Knight":
        armour_list = [
            Armour(part=a["part"], protection=a["protection"])
            for a in config.get("armour", [])
        ]

        weapon_cfg = config["weapon"]
        weapon = Weapon(
            name=weapon_cfg["name"],
            power=weapon_cfg["power"],
        )

        potion_cfg = config.get("potion")
        potion = None
        if potion_cfg is not None:
            potion = Potion(
                name=potion_cfg["name"],
                effect=potion_cfg["effect"],
            )

        return cls(
            name=config["name"],
            base_hp=config["hp"],
            base_power=config["power"],
            armour=armour_list,
            weapon=weapon,
            potion=potion,
        )

    def final_stats(self) -> Dict[str, int]:
        hp = self.base_hp
        power = self.base_power
        protection = sum(a.protection for a in self.armour)

        if self.weapon is not None:
            power += self.weapon.power

        if self.potion is not None:
            for stat, value in self.potion.effect.items():
                if stat == "hp":
                    hp += value
                elif stat == "power":
                    power += value
                elif stat == "protection":
                    protection += value

        return {
            "hp": hp,
            "power": power,
            "protection": protection,
        }
