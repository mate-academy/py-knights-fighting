from typing import Optional, Dict, Any

from app.equipment.armours import ARMOURS
from app.equipment.potions import POTIONS
from app.equipment.weapons import WEAPONS


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config.get("power", 0)
        self.protection = 0
        self.raw_config = config

    def prepare(
        self,
        weapons: Dict[str, Any] = WEAPONS,
        armours: Dict[str, Any] = ARMOURS,
        potions: Dict[str, Any] = POTIONS,
    ) -> None:
        if not isinstance(weapons, dict):
            raise TypeError("weapons must be dict")
        if not isinstance(armours, dict):
            raise TypeError("armours must be dict")
        if not isinstance(potions, dict):
            raise TypeError("potion must be dict")
        if self.raw_config is None:
            raise ValueError("raw_config is required")

        # --- weapon ---
        weapon_cfg = None
        weapon_field = self.raw_config.get("weapon")
        if weapon_field is None:
            raise ValueError("missing weapon")
        elif isinstance(weapon_field, dict):
            # najpierw używamy bezpośrednio power z configu
            if "power" in weapon_field or "damage" in weapon_field:
                weapon_cfg = weapon_field
            elif "name" in weapon_field:
                weapon_cfg = weapons.get(weapon_field["name"])
        elif isinstance(weapon_field, str):
            weapon_cfg = weapons.get(weapon_field)

        if weapon_cfg is None:
            raise ValueError(f"unknown weapon: {weapon_field}")
        self.apply_weapon(weapon_cfg)

        # --- armour ---
        armour_list = self.raw_config.get("armour", [])
        self.apply_armour(armour_list, armours)

        # --- potion ---
        potion_cfg = None
        potion_field = self.raw_config.get("potion")
        if potion_field is None:
            potion_cfg = None
        elif isinstance(potion_field, dict):
            if "effect" in potion_field:
                potion_cfg = potion_field
            elif "name" in potion_field:
                potion_cfg = potions.get(potion_field["name"])
        elif isinstance(potion_field, str):
            potion_cfg = potions.get(potion_field)

        if potion_field is not None and potion_cfg is None:
            raise ValueError(f"unknown potion: {potion_field}")
        self.apply_potion(potion_cfg)

    def apply_weapon(self, weapon: dict) -> None:
        if not isinstance(weapon, dict):
            raise TypeError("apply_weapon expects dict")
        name = weapon.get("name")
        if name is None:
            raise ValueError("weapon must have name")
        self.power += weapon.get("power", 0)
        self.weapon_name = name

    def apply_armour(
        self,
        armour: list[dict],
        armours_dict: Dict[str, Any] = ARMOURS,
    ) -> None:
        if not armour:
            return

        for item in armour:
            if isinstance(item, dict) and "protection" in item:
                self.protection += item["protection"]
                continue

            if isinstance(item, dict) and "part" in item:
                part_name = item["part"]
            elif isinstance(item, str):
                part_name = item
            else:
                continue

            protection = armours_dict.get(part_name, {}).get("protection", 0)
            self.protection += protection

    def apply_potion(self, potion: Optional[dict]) -> None:
        if potion is None:
            return
        effect = potion.get("effect", {})
        if not isinstance(effect, dict):
            return
        for key, value in effect.items():
            if key == "hp":
                self.hp += value
            elif key == "power":
                self.power += value
            elif key == "protection":
                self.protection += value

    def to_stats(self) -> dict:
        return {
            "name": self.name,
            "hp": self.hp,
            "power": self.power,
            "protection": self.protection,
        }
