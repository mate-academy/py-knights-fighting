class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def get_power(self, confiqs: dict) -> None:
        if confiqs["weapon"]["power"] is not None:
            self.power += confiqs["weapon"]["power"]
        if confiqs["potion"] is not None:
            if "power" in confiqs["potion"]["effect"]:
                self.power += confiqs["potion"]["effect"]["power"]

    def get_hp(self, confiqs: dict) -> None:
        if confiqs["potion"] is not None:
            if "hp" in confiqs["potion"]["effect"]:
                self.hp += confiqs["potion"]["effect"]["hp"]

    def get_protection(self, confiqs: dict) -> None:
        if confiqs["armour"] is not None:
            for armour in confiqs["armour"]:
                self.protection += armour["protection"]
        if confiqs["potion"] is not None:
            if "protection" in confiqs["potion"]["effect"]:
                self.protection += confiqs["potion"]["effect"]["protection"]
