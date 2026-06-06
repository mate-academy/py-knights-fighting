class Poison:
    def __init__(self,
                 name: str,
                 hp_affect: int | None = None,
                 power_affect: int | None = None,
                 protection_affect: int | None = None) -> None:
        self.name = name
        self.hp_affect = hp_affect
        self.power_affect = power_affect
        self.protection_affect = protection_affect