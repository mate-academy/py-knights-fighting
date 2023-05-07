from typing import Union, Optional


class Potion:
    def __init__(
            self,
            name: str,
            protection: int = 0,
            hp: int = 0,
            power: int = 0
    ) -> None:
        self.name = name
        self.protection = protection
        self.hp = hp
        self.power = power

    @staticmethod
    def potion_registration(
            knights_potion: Optional[dict] = None
    ) -> Union["Potion", None]:
        if knights_potion is not None:
            effect = knights_potion["effect"]
            protection = effect["protection"] if "protection" in effect else 0
            hp = effect["hp"] if "hp" in effect else 0
            power = effect["power"] if "power" in effect else 0
            return Potion(
                name=knights_potion["name"],
                protection=protection,
                hp=hp,
                power=power
            )
