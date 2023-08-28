class Knight:
    def __init__(
        self, name: str, power: int, hp: int, protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def make_knights(cls, knights: dict) -> dict:
        knights_instances = dict()
        for knight in knights:
            cur_knight = knights[knight]
            name = cur_knight["name"]
            power = cur_knight["power"] + cur_knight["weapon"]["power"]
            hp = cur_knight["hp"]
            protection = 0

            for armour in cur_knight["armour"]:
                protection += armour["protection"]

            if cur_knight["potion"] is not None:
                if "power" in cur_knight["potion"]["effect"]:
                    power += cur_knight["potion"]["effect"]["power"]

                if "protection" in cur_knight["potion"]["effect"]:
                    protection += cur_knight["potion"]["effect"]["protection"]

                if "hp" in cur_knight["potion"]["effect"]:
                    hp += cur_knight["potion"]["effect"]["hp"]

            key = name.lower().replace(" ", "_")

            knights_instances[key] = cls(name, power, hp, protection)

        return knights_instances
