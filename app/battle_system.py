from typing import Tuple

from .knight import Knight


class BattleSystem:
    """
    Provides functionality to simulate battles between knights.

    This class contains static methods for calculating damage, conducting
    individual fight rounds, and simulating full fights between two knights.
    It uses the attributes and methods of the Knight class to manage
    the states and outcomes of battles.
    """

    @staticmethod
    def calculate_damage(attacker: Knight, defender: Knight) -> int:
        """
        Calculates the damage dealt by an attacker to a defender.

        The computation is based on the difference between the attacker's
        power and the defender's protection. If the result is negative,
        the damage will default to zero.

        :param attacker: The attacking knight whose power determines
            the initial damage.
        :type attacker: Knight
        :param defender: The defending knight whose protection reduces
            the attacker's power.
        :type defender: Knight
        :return: The calculated damage inflicted, which will always be
            zero or a positive integer.
        :rtype: int
        """
        damage = attacker.power - defender.protection

        return max(0, damage)

    @staticmethod
    def fight_round(knight1: Knight, knight2: Knight) -> None:
        """
        Conducts a single round of combat between two knights.

        This method simulates one round of battle where both knights
        simultaneously attack each other. Each knight deals damage to
        their opponent based on their power minus the opponent's protection.
        The damage is then applied to both knights' health points.

        :param knight1: The first knight participating in the combat round.
                       This knight will receive damage from knight2 and
                       deal damage to knight2.
        :type knight1: Knight
        :param knight2: The second knight participating in the combat round.
                       This knight will receive damage from knight1 and
                       deal damage to knight1.
        :type knight2: Knight
        :return: None. This method modifies the health points of both
                 knights in place through their take_damage method.
        :rtype: None
        """
        damage_to_knight2 = BattleSystem.calculate_damage(knight1, knight2)
        damage_to_knight1 = BattleSystem.calculate_damage(knight2, knight1)

        knight1.take_damage(damage_to_knight1)
        knight2.take_damage(damage_to_knight2)

    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> Tuple[Knight, Knight]:
        """
        Simulates a fight between two knights using the BattleSystem.

        This static method takes two knights and executes a fight round
        using the BattleSystem. After the fight round is conducted, it
        returns the state of both knights.

        :param knight1: The first knight participating in the fight.
        :type knight1: Knight
        :param knight2: The second knight participating in the fight.
        :type knight2: Knight
        :return: A tuple containing the updated states of knight1 and knight2
                 after the fight round.
        :rtype: Tuple[Knight, Knight]
        """
        BattleSystem.fight_round(knight1, knight2)

        return knight1, knight2
