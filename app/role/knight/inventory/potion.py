from dataclasses import dataclass

from app.role.interfaces import PotionTarget


@dataclass
class Potion:
    name: str
    effect: dict

    def apply_effect(self, knight: PotionTarget) -> None:
        if "power" in self.effect:
            knight.power += self.effect["power"]

        if "protection" in self.effect:
            knight.protection += self.effect["protection"]

        if "hp" in self.effect:
            knight.hp += self.effect["hp"]
