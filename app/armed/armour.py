class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


if __name__ == "__main__":
    armours = {
        "helmet_15": Armour("helmet", 15),
        "breastplate_20": Armour("breastplate", 20),
        "boots_10": Armour("boots", 10),
        "breastplate_15": Armour("breastplate", 15),
        "breastplate_25": Armour("breastplate", 25)
    }

    for a_type, armour in sorted(armours.items()):
        print(f"{a_type} = {armour.__dict__}")
