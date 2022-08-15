from app.knights.knight import Knight
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


def preparing_for_battle():

    for person in list(Knight.all_knights.values()):

        # armour
        if person.armour:
            for armour in person.armour:
                armour_name = f"{armour['part']}_{armour['protection']}"
                if armour_name not in Armour.possible_armour:
                    Armour(armour["part"], armour["protection"])

                Armour.apply_armour(Armour.possible_armour[armour_name],
                                    person)

        # weapon
        if person.weapon["name"] not in Weapon.possible_weapon:
            Weapon(person.weapon["name"], person.weapon["power"])
        Weapon.apply_weapon(Weapon.possible_weapon[person.weapon["name"]],
                            person)

        # potion
        if person.potion is not None:
            if person.potion["name"] not in Potion.possible_potion:
                Potion(person.potion["name"], person.potion["effect"])
            Potion.apply_potion(Potion.possible_potion[person.potion["name"]],
                                person)
