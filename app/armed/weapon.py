class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


if __name__ == "__main__":
    weapons = {
        "lancelot": Weapon(name="Metal Sword", power=50),
        "arthur": Weapon(name="Two-handed Sword", power=55),
        "mordred": Weapon(name="Poisoned Sword", power=60),
        "red_knight": Weapon(name="Sword", power=45)
    }

    for weapon_name, weapon in weapons.items():
        print(f"{weapon_name} = {weapon.__dict__}")
