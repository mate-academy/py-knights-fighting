class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect
        for name in ["hp", "power", "protection"]:
            if name not in self.effect.keys():
                self.effect[name] = 0

    def __dict__(self) -> dict:
        return {
            "name": self.name,
            "effect": {
                key: value for key, value in self.effect.items() if value
            }
        }

    def __repr__(self) -> str:
        return str(self.__dict__())
