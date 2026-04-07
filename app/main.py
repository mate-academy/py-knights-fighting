from typing import Dict, List, Any, Optional


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Dict[str, Any]],
        weapon: Dict[str, Any],
        potion: Optional[Dict[str, Any]] = None
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self._apply_pre_battle_stats()

    def _apply_pre_battle_stats(self) -> None:
        self.protection = sum(item["protection"] for item in self.armour)

        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def receive_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp -= damage

        if self.hp < 0:
            self.hp = 0


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    knights = {
        name: Knight(**stats)
        for name, stats in knights_config.items()
    }

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot_final_power = lancelot.power
    mordred_final_power = mordred.power

    lancelot.receive_damage(mordred_final_power)
    mordred.receive_damage(lancelot_final_power)

    arthur_final_power = arthur.power
    red_knight_final_power = red_knight.power

    arthur.receive_damage(red_knight_final_power)
    red_knight.receive_damage(arthur_final_power)

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
