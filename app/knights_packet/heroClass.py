from __future__ import annotations


class Hero():
    list_hero = []
    hero_dict = {}

    def __init__(self, hero_dict: dict) -> None:
        Hero.hero_dict = hero_dict
        for key, value in self.hero_dict.items():
            Hero.list_hero.append(key.lower())

    def apply_armour(self) -> Hero:
        for key, herro in Hero.hero_dict.items():
            herro["protection"] = 0
            for arrmor in herro["armour"]:
                herro["protection"] += arrmor["protection"]
        return self

    def apply_weapons(self) -> Hero:
        for key, herro in Hero.hero_dict.items():
            herro["power"] += herro["weapon"]["power"]
        return self

    def apply_potion(self) -> None:
        for key, herro in Hero.hero_dict.items():
            if herro["potion"] is not None:
                if "power" in herro["potion"]["effect"]:
                    herro["power"] += herro["potion"]["effect"]["power"]

                if "protection" in herro["potion"]["effect"]:
                    herro["protection"] += (
                        herro)["potion"]["effect"]["protection"]

                if "hp" in herro["potion"]["effect"]:
                    herro["hp"] += herro["potion"]["effect"]["hp"]
