class Health:
    def __init__(self, info: dict) -> None:
        self.hp = info["hp"]
        self.potion = info["potion"]

    def get_hp(self) -> int:
        if self.potion is not None:
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
        return self.hp
