class Armor:
    def __init__(self, info: dict) -> None:
        self.armour = info["armour"]
        self.potion = info["potion"]

    def protection(self) -> int:
        self.protection = sum(a["protection"] for a in self.armour)
        if self.potion is not None:
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
        return self.protection
