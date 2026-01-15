from __future__ import annotations
from app.knights_packet.knights import KNIGHTS
from app.knights_packet.heroClass import Hero


def battle(dict_hero: KNIGHTS) -> dict:
    herros = Hero(dict_hero)
    Hero.apply_armour(herros)
    Hero.apply_weapons(herros)
    Hero.apply_potion(herros)
    Hero.hero_dict["lancelot"]["hp"] -= \
        (Hero.hero_dict["mordred"]["power"]
         - Hero.hero_dict["lancelot"]["protection"])
    Hero.hero_dict["mordred"]["hp"] -= (
        Hero.hero_dict["lancelot"]["power"]
        - Hero.hero_dict["mordred"]["protection"])

    # check if someone fell in battle
    if Hero.hero_dict["lancelot"]["hp"] <= 0:
        Hero.hero_dict["lancelot"]["hp"] = 0

    if Hero.hero_dict["mordred"]["hp"] <= 0:
        Hero.hero_dict["mordred"]["hp"] = 0

    # 2 Arthur vs Red Knight:
    Hero.hero_dict["arthur"]["hp"] -= (
        Hero.hero_dict["red_knight"]["power"]
        - Hero.hero_dict["arthur"]["protection"])
    Hero.hero_dict["red_knight"]["hp"] -= (
        Hero.hero_dict["arthur"]["power"]
        - Hero.hero_dict["red_knight"]["protection"])

    # check if someone fell in battle
    if Hero.hero_dict["arthur"]["hp"] <= 0:
        Hero.hero_dict["arthur"]["hp"] = 0

    if Hero.hero_dict["red_knight"]["hp"] <= 0:
        Hero.hero_dict["red_knight"]["hp"] = 0

    # Return battle results:
    return {
        Hero.hero_dict["lancelot"]["name"]:
            Hero.hero_dict["lancelot"]["hp"],
        Hero.hero_dict["arthur"]["name"]:
            Hero.hero_dict["arthur"]["hp"],
        Hero.hero_dict["mordred"]["name"]:
            Hero.hero_dict["mordred"]["hp"],
        Hero.hero_dict["red_knight"]["name"]:
            Hero.hero_dict["red_knight"]["hp"],
    }
