from app.knight.knight import Knight
from app.knights_equipment.armour import Armour
from app.knights_equipment.potion import Potion
from app.knights_equipment.weapon import Weapon


class Battle:

    @staticmethod
    def knight_prepares_for_battle(knight: dict) -> Knight:
        """
        init weapon, armour and potion objects and init knight object
        """

        weapon = Weapon(knight["weapon"]["name"], knight["weapon"]["power"])

        armours = []
        for armour in knight["armour"]:
            armours.append(
                Armour(armour["part"], armour["protection"])
            )

        if knight["potion"] is not None:
            potion = (
                Potion(knight["potion"]["name"], knight["potion"]["effect"])
            )
        else:
            potion = None

        return Knight(
            knight["name"],
            knight["power"],
            knight["hp"],
            armours,
            weapon,
            potion
        )

    @staticmethod
    def calculate_stats_before_duel(
            first_knight: Knight,
            second_knight: Knight
    ) -> None:
        """
        calculate stats of knight's before attack stage
        """

        first_knight.calculate_power()
        second_knight.calculate_power()
        first_knight.calculate_protection()
        second_knight.calculate_protection()
        first_knight.calculate_hp()
        second_knight.calculate_hp()

    @staticmethod
    def knight_attack(first_knight: Knight, second_knight: Knight) -> None:
        """
        method calculate how much attack is blocked by knight protection
        and how much HP attacked knight will lose
        """

        attack_blocking = first_knight.power - second_knight.protection
        second_knight.hp -= attack_blocking

    @staticmethod
    def knights_duel(first_knight: Knight, second_knight: Knight) -> dict:
        """
        1. first knight attack second
        2. second attack first
        3. check death
        4. return result of duel
        """

        Battle.calculate_stats_before_duel(first_knight, second_knight)
        Battle.knight_attack(first_knight, second_knight)
        Battle.knight_attack(second_knight, first_knight)

        if first_knight.hp <= 0:
            first_knight.hp = 0
        elif second_knight.hp <= 0:
            second_knight.hp = 0

        duel_results = {
            first_knight.name: first_knight.hp,
            second_knight.name: second_knight.hp
        }
        print(duel_results)
        return duel_results

    @staticmethod
    def knights_tournament(duel_couples: list[list]) -> dict:
        """
        method makes duel for every duel part and return results
        """

        tournament_result = {}
        for index, duel_couple in enumerate(duel_couples):
            duel_result = Battle.knights_duel(
                duel_couple[index][0],
                duel_couple[index][1]
            )
            tournament_result = {**duel_result}

        print(tournament_result)
        return tournament_result
