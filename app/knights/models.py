from typing import Optional


class Knight:
    def __init__(
        self,
        name: str,
        hp: int,
        power: int,
        armour: Optional[list[dict]],
        weapon: Optional[dict],
        potion: Optional[dict],
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def prepare_stats(self) -> dict[str, int]:
        potion_effect = (self.potion or {}).get("effect", {})

        protection = sum(
            part.get("protection", 0)
            for part in (self.armour or [])
        )
        protection += potion_effect.get("protection", 0)

        weapon_power = (self.weapon or {}).get("power", 0)

        total_power = (
            self.power
            + weapon_power
            + potion_effect.get("power", 0)
        )

        hp = self.hp + potion_effect.get("hp", 0)

        return {
            "hp": hp,
            "power": total_power,
            "protection": protection,
        }
