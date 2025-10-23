class Potion:

    def __init__(self,
                 name: str | None = None,
                 hp: int | None = None,
                 power: int | None = None,
                 protection: int | None = None
                 ):
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def potion(self) -> dict | None:
        if not any([self.name,
                    self.hp,
                    self.power,
                    self.protection]):
            return None
        else:
            return {
                "name": self.name,
                "effect":
                    {
                        {
                            "hp": self.hp,
                            "power": self.power,
                            "protection": self.protection
                        }
                    }
                }

