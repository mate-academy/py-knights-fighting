class Potion:
    def __init__(self, name: str, potion_info: dict) -> None:
        self.name = name
        self.protection = 0

        for key, value in potion_info.items():
            setattr(self, key, value)
