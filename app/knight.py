from app.knights_params import armor
from app.knights_params import weapon
from app.knights_params import potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

        Knight.knights.add(self)

    knights = set()

    def take_a_weapon(self, name: str) -> object:
        # add power from take a weapon
        self.power += weapon.value[name][0]["power"]
        return weapon.value[name][0]["power"]

    def dress_on_armors(self, name: str) -> list:
        # add hp from dress on an armor
        total_armor = []
        for el in armor.value[name]:
            self.hp += el["protection"]
            total_armor.append(el["protection"])
        return total_armor

    def drink_potions(self, name: str) -> tuple:
        # add hp & power from drink potion
        _pr, _pn, _hp = "", "", ""
        if potion.value[name] is None:
            pass
        else:
            if "power" in potion.value[name]["effect"]:
                self.power += potion.value[name]["effect"]["power"]
                _pr = "Power: " + str(
                    potion.value[name]["effect"]["power"])
            if "protection" in potion.value[name]["effect"]:
                self.hp += potion.value[name]["effect"]["protection"]
                _pn = "Protection: " + str(potion.value[name]["effect"][
                                               "protection"])
            if "hp" in potion.value[name]["effect"]:
                self.hp += potion.value[name]["effect"]["hp"]
                _hp = "HP: " + str(
                    potion.value[name]["effect"][
                        "hp"])
        return _hp, _pr, _pn

    @staticmethod
    def show_base_values(first: "Knight", second: "Knight") -> None:
        # Just show base knight value
        print("{0:^67}".format(f"Health point: {first.hp}"),
              "{0:^67}".format(f"Health point: {second.hp}"))
        print("{0:^67}".format(f"Power: {first.power}"),
              "{0:^67}".format(f"Power: {second.power}"))

    @classmethod
    def versus(cls, first_fighter: str, second_fighter: str) -> None:
        # Choices first and second fighters between all knights
        for el in Knight.knights:
            if el.name == first_fighter:
                first_fighter = el
            if el.name == second_fighter:
                second_fighter = el

        print("*" * 135)
        print("{:^135}".format(f"({first_fighter}) "
                               f"{first_fighter.name}"
                               f" --- VS --- "
                               f"{second_fighter.name} "
                               f"({second_fighter}) "))
        print("*" * 135)

        # show base values
        print("{:^135}".format("Base values:"))
        Knight.show_base_values(first_fighter, second_fighter)

        # show values after dress on an armor
        _1 = ("After dress on an armor, "
              "health point and protection add new values:")
        print("\n{:^135}".format(_1))

        _1 = Knight.dress_on_armors(first_fighter, first_fighter.name.lower())
        _2 = (Knight.dress_on_armors
              (second_fighter, second_fighter.name.lower()))
        print(("{0:^67}".format(
            f"{_1}")),
            ("{0:^67}".format(
                f"{_2}")))

        # show values after take a weapon
        print("\n{:^135}".format("After take a weapon, "
                                 "power add new values:"))
        _1 = Knight.take_a_weapon(first_fighter, first_fighter.name.lower())
        _2 = Knight.take_a_weapon(second_fighter, second_fighter.name.lower())
        print(("{0:^67}".format(
            f"{_1}")),
            ("{0:^67}".format(
                f"{_2}")))

        # show values after drink a potion
        print("\n{:^135}".format(
            " Add new values after potion drink:"))

        _1 = Knight.drink_potions(first_fighter, first_fighter.name.lower())
        _2 = Knight.drink_potions(second_fighter, second_fighter.name.lower())
        print(("{0:^67}".format(
            f"{_1}")),
            ("{0:^67}".format(
                f"{_2}")))

        print("*" * 135)

        # battle calculation, check if someone fell in battle
        # from first fighter
        result = first_fighter.hp - second_fighter.power
        if result > 0:
            print(
                f"{first_fighter.name} is not fell, "
                f"his health point is: {result}")
        else:
            print(
                f"{first_fighter.name} is fell, "
                f"his health point is: {result}")

        # from second fighter
        result = second_fighter.hp - first_fighter.power
        if result > 0:
            print(
                f"{second_fighter.name} is not fell, "
                f"his health point is: {result}")
        else:
            print(
                f"{second_fighter.name} is fell, "
                f"his health point is: {result}")
