from dataclasses import dataclass


@dataclass
class Armour:
    part: str
    protection: int

    @classmethod
    def create(cls, dict_: dict) -> list | None:
        if dict_["armour"]:
            res = []
            for piece in dict_["armour"]:
                res.append(cls(piece["part"], piece["protection"]))
            return res
