class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight.get("name")
        self.power = knight.get("power")
        self.hp = knight.get("hp")
        self.armour = knight.get("armour")
        self.weapon = knight.get("weapon")
        self.potion = knight.get("potion")
        self.protection = 0

    def prepare_for_battle(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)
        self.power += self.weapon["power"]
        if self.potion:
            for attribute in (effects := self.potion["effect"]):
                setattr(
                    self,
                    attribute,
                    getattr(self, attribute) + effects[attribute]
                )
