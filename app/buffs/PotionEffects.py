class PotionEffects:
    def __init__(self, hp: int, power: int, protection: int) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Effect: hp = {self.hp}," \
               f" power = {self.power}," \
               f" protection = {self.protection}"
