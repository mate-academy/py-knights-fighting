class Potion:
    """effect may contain power, hp, protection"""

    name: str
    effect: tuple[int, int, int]

    def __init__(self, potion: dict) -> None:
        if potion:
            self.name = potion.get("name")
            effect = potion.get("effect")
            if effect:
                self.effect = (
                    effect.get("power", 0),
                    effect.get("hp", 0),
                    effect.get("protection", 0),
                )
            else:
                self.effect = (0, 0, 0)
        else:
            self.name = ""
            self.effect = (0, 0, 0)
