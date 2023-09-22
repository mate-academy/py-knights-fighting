class Weapon:

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


metal_sword = Weapon("Metal Sword", 50)
two_handed_sword = Weapon("Two-handed Sword", 55)
poisoned_sword = Weapon("Poisoned Sword", 60)
sword = Weapon("Sword", 45)
