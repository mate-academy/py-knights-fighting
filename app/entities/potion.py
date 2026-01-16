class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def apply(self, knight: "Knight") -> None:
        for key, value in self.effect.items():
            if key == "hp":
                knight.hp += value
            elif key == "power":
                knight.power += value
            elif key == "protection":
                for armor in knight.armor:
                    armor.protection += value
