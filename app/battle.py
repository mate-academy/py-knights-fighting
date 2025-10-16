from .knight import Knight


class Battle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def prepare_for_fight(self) -> None:
        for knight in (self.first_knight, self.second_knight):
            knight.apply_armour()
            knight.apply_potion()
            knight.apply_weapon()

    def check_hp(self, knight: Knight) -> int:
        return 0 if knight.hp <= 0 else knight.hp

    def perform_attack(self, attacker: Knight, defender: Knight) -> None:
        damage = attacker.power - defender.protection
        if damage > 0:
            defender.hp -= damage

    def fight(self) -> dict[str, int]:
        self.perform_attack(self.second_knight, self.first_knight)
        self.perform_attack(self.first_knight, self.second_knight)

        first_knight_hp = self.check_hp(self.first_knight)
        second_knight_hp = self.check_hp(self.second_knight)

        return {
            self.first_knight.name: first_knight_hp,
            self.second_knight.name: second_knight_hp,
        }
