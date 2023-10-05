class Character:
    def __init__(self, character: dict) -> None:
        self.name = character["name"]
        self.hp = character["hp"]
        self.protection = sum([
            part["protection"]
            for part in character["armour"]
        ])
        self.power = character["power"] + character["weapon"]["power"]
        self.drink_potion(character)

    def drink_potion(self, character: dict) -> None:
        if character["potion"] is not None:
            if "power" in character["potion"]["effect"]:
                self.power += character["potion"]["effect"]["power"]
            if "protection" in character["potion"]["effect"]:
                self.protection += character["potion"]["effect"]["protection"]
            if "hp" in character["potion"]["effect"]:
                self.hp += character["potion"]["effect"]["hp"]

    def is_fell_in_battle(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def battle_results(self) -> dict:
        return {self.name: self.hp}
