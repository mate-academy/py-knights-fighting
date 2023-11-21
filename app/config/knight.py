class Knight:
    persons = {}

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
        self.persons[name] = self

    def calculations(self, state: dict) -> None:
        self.power += state["weapon"]["power"]
        for armour_set in state["armour"]:
            self.protection += armour_set["protection"]
        if state["potion"] is not None:
            if "power" in state["potion"]["effect"]:
                self.power += state["potion"]["effect"]["power"]
            if "hp" in state["potion"]["effect"]:
                self.hp += state["potion"]["effect"]["hp"]
            if "protection" in state["potion"]["effect"]:
                self.protection += state["potion"]["effect"]["protection"]
