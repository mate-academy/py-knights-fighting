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
    def potion_registration(knights_potion: dict = None) -> "Potion" or None:
        if knights_potion is not None:
            effect = knights_potion["effect"]
            protection = 0
            if "protection" in effect:
                protection = effect["protection"]
            hp = 0
            if "hp" in effect:
                hp = effect["hp"]
            power = 0
            if "power" in effect:
                power = effect["power"]
            return Potion(
                name=knights_potion["name"],
                protection=protection,
                hp=hp,
                power=power
            )
        else:
            return None
