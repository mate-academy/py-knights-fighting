class Potion:
    def __init__(
            self,
            potion_dict: dict[
                str,
                str | dict[str, int]
            ]
    ) -> None:
        self.name: str = potion_dict.get("name")
        self.effect: dict[str, int] = potion_dict.get("effect")
