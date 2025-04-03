from typing import List


class Knight:
    def __init__(self, name: str, hp: int, armour: List[dict], potion: dict = None):
        self.name = name
        self.hp = hp
        self.armour = armour
        self.potion = potion
        self.knight_config = {
            "hp": hp,
            "armour": armour
        }
        if potion:
            self.knight_config["potion"] = potion

    def get_hp_of_knight(self) -> int:
    # Отримуємо базове HP лицаря
        hp = self.knight_config["hp"]
    # Якщо є зілля і ефект з HP, додаємо його до базового HP
        if self.potion:
            return hp + self.potion.get("effect", {}).get("hp", 0)
        return hp


def get_power_of_knight(knight: Knight) -> int:
    # Отримуємо базову потужність лицаря
    power = knight.knight_config.get("power", 0)
    # Отримуємо потужність зброї
    weapon_power = knight.knight_config.get("weapon", {}).get("power", 0)
    # Якщо є зілля і в ньому є ефект для power, додаємо його
    if knight.potion:
        power += knight.potion.get("effect", {}).get("power", 0)
    # Повертаємо суму базової потужності і потужності зброї
    return power + weapon_power


def get_protection_of_knight(knight: Knight) -> int:
    # Отримуємо всю броню лицаря
    armour = knight.knight_config["armour"]
    # Підсумовуємо захист від кожного елементу броні
    total_protection = sum(equip["protection"] for equip in armour)
    # Якщо є зілля і в ньому є ефект захисту, додаємо його до загального захисту
    if knight.potion:
        total_protection += knight.potion.get("effect", {}).get("protection", 0)

    return total_protection


def get_hp_of_knight(knight: Knight) -> int:
    # Отримуємо базове HP лицаря
    hp = knight.knight_config["hp"]
    # Якщо є зілля і ефект з HP, додаємо його до базового HP
    if knight.potion:
        return hp + knight.potion.get("effect", {}).get("hp", 0)
    return hp
