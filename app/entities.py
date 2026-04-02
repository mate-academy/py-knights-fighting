from typing import Dict, Any


class Knight:
    def __init__(self, config_dict: Dict[str, Any]) -> None:
        self._base_hp = config_dict.get("hp", 100)
        self._base_power = config_dict.get("power", 0)
        self.name = config_dict.get("name")
        self.armour = config_dict.get("armour", [])
        self.weapon = config_dict.get("weapon")
        self.potion = config_dict.get("potion")
        self.hp = self._base_hp
        self.power = self._base_power
        self.protection = 0
        self._prepared = False

    def prepare(self) -> None:
        """Merges all stats from gear and potions once."""
        if self._prepared:
            return

        armour_protection = sum(p.get("protection", 0) for p in self.armour)
        weapon_power = (self.weapon or {}).get("power", 0)
        effect = (self.potion or {}).get("effect", {})
        self.hp = self._base_hp + self._to_num(effect.get("hp", 0))
        self.power = (self._base_power + weapon_power
                      + self._to_num(effect.get("power", 0)))
        self.protection = (armour_protection
                           + self._to_num(effect.get("protection", 0)))
        self._prepared = True

    @staticmethod
    def _to_num(value: Any) -> int | float:
        return value if isinstance(value, (int, float)) else 0

    def take_damage(self, opponent_power: int) -> None:
        damage = max(opponent_power - self.protection, 0)
        self.hp = max(self.hp - damage, 0)

    def _calc_armour_protection(self) -> float:
        return sum(p.get("protection", 0) for p in self.armour or [])

    def _weapon_power(self) -> int:
        return (self.weapon or {}).get("power", 0)

    def _apply_potion_to(
            self, hp: int, power: int, protection: int
    ) -> tuple[int, int, int]:
        # Default to an empty dict if self.potion or "effect" is missing
        effect = (self.potion or {}).get("effect", {})

        return (
            hp + effect.get("hp", 0),
            power + effect.get("power", 0),
            protection + effect.get("protection", 0)
        )
