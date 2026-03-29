from typing import Callable, Dict, List, Optional


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Dict[str, int]],
        weapon: Dict[str, int],
        potion: Optional[Dict[str, Dict[str, int]]]
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    @staticmethod
    def check_health(method: Callable[["Knight"], None]
                     ) -> Callable[["Knight"], None]:
        def wrapper(self: "Knight") -> None:
            result = method(self)
            if self.hp < 0:
                self.hp = 0
            return result
        return wrapper

    @check_health
    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def update_stats(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
