from app.fighters import equipment


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[equipment.Armour] | None,
        weapon: equipment.Weapon,
        potion: equipment.Potion | None
    ) -> None:
        self.protection = 0
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @staticmethod
    def create_list_armour(arm: list[dict] | None)\
            -> list[equipment.Armour] | None:
        if isinstance(arm, list):
            res_armour = []
            for value in arm:
                res_armour.append(equipment.Armour(value["part"],
                                                   value["protection"]))
            return res_armour
        return None

    @staticmethod
    def create_potion(pot: dict | None) -> equipment.Potion | None:
        if pot is not None:
            return equipment.Potion(pot["name"], pot["effect"])
        return None

    def prepare_for_battle(self) -> None:
        if isinstance(self.armour, list):
            for value in self.armour:
                self.protection += value.points
        self.power += self.weapon.points
        if self.potion is not None:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]

    @staticmethod
    def check_name(list_figh: list["Knight"], name_fighter: str) -> "Knight":
        for value in list_figh:
            if value.name == name_fighter:
                return value

    def fight_between_two(self, others: "Knight") -> None:
        if isinstance(others, Knight):
            self.hp -= others.power - self.protection
            others.hp -= self.power - others.protection

    def check_hp(self) -> None:
        if self.hp <= 0:
            self.hp = 0
