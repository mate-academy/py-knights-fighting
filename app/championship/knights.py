class Knight:

    knights = dict()

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def add_knights(cls, knight_stat: dict) -> None:
        # apply base stat
        name = knight_stat["name"]
        hp = knight_stat["hp"]
        protection = 0
        power = knight_stat["power"]

        # apply armour
        if knight_stat["armour"]:
            protection = sum(
                [part["protection"] for part in knight_stat["armour"]]
            )

        # apply weapon
        if knight_stat["weapon"]:
            power += knight_stat["weapon"]["power"]

        # apply potion if exist
        if knight_stat["potion"]:
            for potion, effect in knight_stat["potion"]["effect"].items():
                if potion == "power":
                    power += effect
                if potion == "protection":
                    protection += effect
                if potion == "hp":
                    hp += effect

        # create instance
        cls.knights[name] = cls(
            name,
            power,
            hp,
            protection
        )
