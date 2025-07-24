from app.units.knight import Knight


class Preparation:
    def __init__(self) -> None:
        pass

    @staticmethod
    def calculate_stats(name: str, knights: dict) -> tuple:
        hp = knights[name]["hp"]
        print(f"{knights[name]} {knights[name]["hp"]} {hp}")
        power = knights[name]["power"]
        protection = 0

        armour = knights[name]["armour"]
        weapon = knights[name]["weapon"]
        potion = knights[name]["potion"]

        for piece in armour:
            if piece.get("protection"):
                protection += piece["protection"]

        if weapon and weapon.get("power"):
            power += weapon["power"]

        if potion and potion.get("effect"):
            effects = potion["effect"]

            for effect, value in effects.items():
                if effect == "power":
                    power += value
                elif effect == "hp":
                    hp += value
                elif effect == "protection":
                    protection += value

        return hp, power, protection

    @staticmethod
    def set_knight(name: str, knights: dict) -> Knight | str:
        if name not in knights:
            return f"{name} is not in knights list."

        new_name = knights[name]["name"]
        hp, power, protection = Preparation.calculate_stats(name, knights)

        return Knight(new_name, hp, power, protection)
