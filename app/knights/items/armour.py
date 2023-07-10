from dataclasses import dataclass


@dataclass
class Armour:
    part: str
    protection: int

    @classmethod
    def create(cls, dict_: dict) -> list | None:
        if dict_["armour"]:
            return [
                cls(piece["part"], piece["protection"])
                for piece in dict_["armour"]
            ]
