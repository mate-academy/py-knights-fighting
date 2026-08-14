class Knight:
    def __init__(self, knight_stats: dict) -> None:
        self.name = knight_stats["name"]
        self.power = knight_stats["power"]
        self.hp = knight_stats["hp"]
        self.protection = 0
        self.weapon = Weapon(knight_stats["weapon"], self)
        self.armour = Armour(knight_stats["armour"], self)
        potion = knight_stats.get("potion")
        if potion is None:
            self.potion = potion
        else:
            self.potion = Potion(potion, self)

    def get_ready_for_fight(self) -> None:
        if self.armour:
            self.armour.equip_armour()
        self.weapon.draw_weapon()
        if self.potion:
            self.potion.drink_potion()

    @staticmethod
    def get_knight(dict_of_knights: dict, name: str) -> "Knight":
        return Knight(dict_of_knights[name])


class Armour:
    def __init__(self, list_of_armour: list[dict], owner: "Knight") -> None:
        self.list_of_armour = list_of_armour
        self.owner = owner

    def equip_armour(self) -> None:
        for armor_piece in self.list_of_armour:
            self.owner.protection += armor_piece["protection"]


class Weapon:
    def __init__(self, weapon_dict: dict, owner: "Knight") -> None:
        self.weapon_name = weapon_dict["name"]
        self.weapon_power = weapon_dict["power"]
        self.owner = owner

    def draw_weapon(self) -> None:
        self.owner.power += self.weapon_power


class Potion:
    def __init__(self, potion_dict: dict, owner: "Knight") -> None:
        self.potion_name = potion_dict["name"]
        self.effects = potion_dict["effect"]
        self.owner = owner

    def drink_potion(self) -> None:
        self.owner.hp += self.effects.get("hp", 0)
        self.owner.power += self.effects.get("power", 0)
        self.owner.protection += self.effects.get("protection", 0)
