

class Effect:

    def __init__(
            self,
            power: int | None = None,
            protection: int | None = None,
            hp: int | None = None
    ) -> None:
        if power is not None:
            self.power = power

        if protection is not None:
            self.protection = protection

        if hp is not None:
            self.hp = hp
