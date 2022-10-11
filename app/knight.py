class Knight:

    def __init__(self, name: str, info: dict) -> None:
        self.name = name
        self.info = info

    def get_protection(self) -> int:
        count = 0
        for i in self.info["armour"]:
            count += i["protection"]
        return count

    def get_power(self) -> int:
        count = self.info["power"]
        count += self.info["weapon"]["power"]
        return count

    def characteristics(self) -> dict:
        power = self.get_power()
        protection = self.get_protection()
        hp = self.info["hp"]

        if self.info["potion"]:
            if "power" in self.info["potion"]["effect"]:
                power += self.info["potion"]["effect"]["power"]
            if "protection" in self.info["potion"]["effect"]:
                protection += self.info["potion"]["effect"]["protection"]
            if "hp" in self.info["potion"]["effect"]:
                hp += self.info["potion"]["effect"]["hp"]

        return {"name": self.name,
                "power": power,
                "protect": protection,
                "hp": hp}


def get_characteristics(info: dict) -> list:
    knights = [Knight(value["name"], value) for value in info.values()]
    return [knights[i].characteristics() for i in range(len(knights))]
