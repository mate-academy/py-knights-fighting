class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


if __name__ == "__main__":
    berserk = Potion(name="Berserk",
                     effect={
                         "power": +15,
                         "hp": -5,
                         "protection": +10
                     })
    blessing = Potion(name="Blessing",
                      effect={
                          "hp": +10,
                          "protection": +5
                      })
    print(f"{berserk.name} = {berserk.__dict__}")
    print(f"{blessing.name} = {blessing.__dict__}")
