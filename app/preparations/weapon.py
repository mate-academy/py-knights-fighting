class Weapon:
    def __init__(self, info: dict) -> None:
        self.power = info["power"]
        self.weapon = info["weapon"]
        self.potion = info["potion"]

    def get_power(self) -> int:
        self.power += self.weapon["power"]
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
        return self.power
