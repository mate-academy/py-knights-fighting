class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power + weapon["power"] + (potion["effect"]["power"]
                                                if potion and "power" in potion["effect"] else 0)
        self.hp = hp + (potion["effect"]["hp"] if potion and "hp" in potion["effect"] else 0)
        self.protection = (sum(part["protection"] for part in armour) if armour else 0
                           ) + (
            potion["effect"].get("protection", 0) if potion and "protection" in potion["effect"] else 0
        )


    def __str__(self):
        return f"Knight(name={self.name}, power={self.power}, hp={self.hp}, protection={self.protection})"
    @classmethod
    def config_optimize(cls, config):
        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"]
        )
