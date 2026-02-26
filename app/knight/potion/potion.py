from __future__ import annotations

from app.knight.potion.effect import PotionEffect


class Potion:
    def __init__(
            self,
            name: str,
            effect: PotionEffect
    ) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def get_from_dict(
            cls,
            potion_dict: dict[str, str | dict[str, int]]
    ) -> Potion:
        return cls(
            name=potion_dict.get("name"),
            effect=PotionEffect.get_from_dict(potion_dict.get("effect"))
        )
