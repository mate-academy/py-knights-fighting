# import random
from app.Equipment.potion import Potion
from app.Equipment.final_stats import Stats
from app.Equipment.gear_box import Armor, Weapon

knights = {}
armour = {}
weapon = {}
potion = {}


def manage_equipment(heroes: dict) -> None:
    for knight in heroes:
        hero = heroes[knight]
        knights[f"{knight}"] = Stats(name=hero["name"],
                                     health_points=hero["hp"],
                                     power=hero["power"])

        armour[f"{knight}_arm"] = Armor()
        hero_arm = armour[f"{knight}_arm"]
        if len(hero["armour"]) != 0:
            for part in hero["armour"]:
                if part["part"] == "helmet":
                    hero_arm.helmet = part["protection"]
                if part["part"] == "breastplate":
                    hero_arm.breast = part["protection"]
                if part["part"] == "boots":
                    hero_arm.boots = part["protection"]

        weapon[f"{knight}_wpn"] = Weapon(hero["weapon"]["power"])

        potion[f"{knight}_ptn"] = Potion()
        hero_ptn = potion[f"{knight}_ptn"]
        if hero["potion"] is not None:
            effect = hero["potion"]["effect"]
            for attribute in effect:
                if attribute == "hp":
                    hero_ptn.hp = effect["hp"]
                if attribute == "power":
                    hero_ptn.pwr = effect["power"]
                if attribute == "protection":
                    hero_ptn.ptn = effect["protection"]


def finilize_stats(heroes: dict) -> None:
    """
    to make bring more fun uncomment:
    import, and raws below
    """

    for knight in knights:
        # luck = random.randrange(1000)
        gods_attention_hp = 0
        gods_attention_ptn = 0
        gods_attention_pwr = 0

        # if 40 < luck < 50:
        #     """Goddes gifted you with her smile"""
        #     gods_attention_hp = 30
        #
        # if 50 < luck < 60:
        #     """God encouraged you"""
        #     gods_attention_ptn = 30
        #
        # if 65 < luck < 70:
        #     """Demon likes you"""
        #     gods_attention_pwr = 60
        #     gods_attention_hp = -20
        #
        # if heroes[knight]["potion"] is None:
        #     if 0 < luck < 300:
        #         """You found short sword on the ground"""
        #         weapon[f"{knight}_wpn"].left = 25

        knights[knight].hp += (potion[f"{knight}_ptn"].hp
                               + gods_attention_hp)

        knights[knight].ptn += (armour[f"{knight}_arm"].helmet
                                + armour[f"{knight}_arm"].breast
                                + armour[f"{knight}_arm"].boots
                                + potion[f"{knight}_ptn"].ptn
                                + gods_attention_ptn)

        knights[knight].pwr += (weapon[f"{knight}_wpn"].right
                                + weapon[f"{knight}_wpn"].left
                                + potion[f"{knight}_ptn"].pwr
                                + gods_attention_pwr)
