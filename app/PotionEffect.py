class PotionEffect:
    def __init__(self,
                 power: int = 0,
                 hp: int = 0,
                 protection: int = 0
                 ) -> None:
        self.__power: int = power
        self.__hp: int = hp
        self.__protection: int = protection

    @property
    def power(self) -> int:
        return self.__power

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def protection(self) -> int:
        return self.__protection

    def __repr__(self) -> str:
        return (f"PotionEffect("
                f"power={self.power}, "
                f"hp={self.hp}, "
                f"protection={self.protection})")
