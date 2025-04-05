from typing import Dict


class Potion:
    def __init__(
            self,
            name: str,
            effect: Dict[str, int]
    ) -> None:
        self.name = name
        self.effect = effect

    def get_effect(self) -> Dict[str, int]:
        return self.effect
