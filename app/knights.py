class Knights:

    def __init__(
            self, name: str,
            power: int, hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection


def make_instances(knight: dict) -> list:
    all_knights = []
    for knights in knight.values():
        all_power = knights["power"]
        all_hp = knights["hp"]
        all_protection = 0

        if knights["armour"] is not None:
            for armor in knights["armour"]:
                all_protection += armor["protection"]
        if knights["potion"] is not None:
            for key in knights["potion"]["effect"]:
                value = knights["potion"]["effect"][key]
                if key == "power":
                    all_power += value
                if key == "hp":
                    all_hp += value
                if key == "protection":
                    all_protection += value
        if knights["weapon"] is not None:
            all_power += knights["weapon"]["power"]

        all_knights.append(Knights(
            name=knights["name"],
            hp=all_hp,
            power=all_power,
            protection=all_protection))
    return all_knights
