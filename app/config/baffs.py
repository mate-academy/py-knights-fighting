class Buffs:
    def __init__(self, buffs: dict):
        self.buffs = buffs

    def take_buff(self, knight) -> None:
        if self.buffs is not None:
            if "hp" in self.buffs["effect"]:
                knight.hp += self.buffs["effect"]["hp"]
            if "protection" in self.buffs["effect"]:
                knight.protection += self.buffs["effect"]["protection"]
            if "power" in self.buffs["effect"]:
                knight.power += self.buffs["effect"]["power"]
