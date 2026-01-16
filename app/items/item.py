from app.knight import Knight


class Item:
    def __init__(
            self,
            name: str,
            power_effect: int,
            hp_effect: int,
            protection_effect: int
    ) -> None:
        self.name = name
        self.power_effect = power_effect
        self.hp_effect = hp_effect
        self.protection_effect = protection_effect

    def use_on(self, character: "Knight") -> None:
        character.power += self.power_effect
        character.hp += self.hp_effect
        character.protection += self.protection_effect

        print(f"{self.name} is used on {character.name}")
        character.show_stats()
