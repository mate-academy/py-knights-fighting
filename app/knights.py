from app.weapon import Weapon
from app.potion import Potion


class Knights:
    def __init__(self, knights: dict) -> None:
        self.knights = knights

    def armor_score(self) -> dict:
        for name, armor in self.knights.items():
            armor["protection"] = 0
            if armor["armour"]:
                armor["protection"] += (
                    sum(num["protection"]
                        for num in armor["armour"]))
        weapon = Weapon(self.knights)
        potion = Potion(weapon.weapon_score())
        finish_score = potion.potion_score()
        return finish_score
