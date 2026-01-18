from app.models.knight import Knight


class PreparationToBattle:

    def __init__(self, knight: Knight) -> None:
        self.knight = knight

    def preparation_to_battle(self) -> Knight:
        power = self.knight.power
        weapon = self.knight.weapon
        hp = self.knight.hp
        armours = self.knight.armour
        total_protection = 0
        total_hp = hp
        for armor in armours:
            total_protection += armor.protection
        total_power = power + weapon.power
        potion = self.knight.potion
        if potion is not None:
            potion_hp = potion.effect.get("hp")
            potion_power = potion.effect.get("power")
            potion_protection = potion.effect.get("protection")
            if potion_hp is not None:
                total_hp += potion_hp
            if potion_power is not None:
                total_power += potion_power
            if potion_protection is not None:
                total_protection += potion_protection
        self.knight.power = total_power
        self.knight.hp = total_hp
        self.knight.total_protection = total_protection
        self.knight.total_power = total_power
        return self.knight
