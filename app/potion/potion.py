class Potion:
    def __init__(self, name: str):
        self.name = name
        self.power = 0
        self.hp = 0
        self.protection = 0

    def __repr__(self):
        return self.name

    # create a Potion instance from dictionary with properties
    @classmethod
    def get_potion_cls(cls, potion: dict) -> "Potion":
        if potion is None:
            return cls("Without potion")

        new_cls = cls(potion["name"])

        for quality, quantity in potion["effect"].items():
            setattr(new_cls, quality, quantity)

        return new_cls
