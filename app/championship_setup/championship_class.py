from app.knights_setup.knight_class import Knight
from app.knights_setup.knights_class import Knights


class Championship:
    def __init__(self, knights_config: dict) -> None:
        self.knights_config = knights_config
        self.results = {}

    @staticmethod
    def apply_knight_attributes(knight: Knight) -> Knight:
        """
        Apply knight's extra attributes to main ones (e.g. hp, power).
        :param knight:
        :return: Knight instance
        """
        # apply armour
        knight.protection = 0
        for armour in knight.armour:
            knight.protection += armour["protection"]

        # apply weapon
        knight.power += knight.weapon["power"]

        # apply potion if it exists
        if knight.potion is not None:
            if "power" in knight.potion["effect"]:
                knight.power += knight.potion["effect"]["power"]

            if "protection" in knight.potion["effect"]:
                knight.protection += knight.potion["effect"]["protection"]

            if "hp" in knight.potion["effect"]:
                knight.hp += knight.potion["effect"]["hp"]
        return knight

    def battle_preparation(self) -> dict:
        """
        Create Knight instances, apply their additional attributes and store
        them in the Knights class.
        :return: a dictionary of Knight instances
        """
        raw_knight_instances = {knight_name: Knight(**knight_attributes)
                                for knight_name, knight_attributes in
                                self.knights_config.items()}
        for raw_knight_name, raw_knight in raw_knight_instances.items():
            Knights.add_knight(
                raw_knight_name,
                self.apply_knight_attributes(raw_knight)
            )
        return Knights.knights

    @staticmethod
    def championship_results() -> dict:
        """
        Display the final result of all Knights.
        :return: a dictionary of Knight instances
        """
        results = {knight.name: knight.hp
                   for knight in Knights.knights.values()}
        return results

    @staticmethod
    def single_battle(*knights: tuple[Knight, Knight]) -> dict:
        """
        Carry out a battle between two Knight instances and fix the results.
        :param knights:
        :return: a dictionary of Knight instances
        """
        for i in range(len(knights)):
            knights[i].hp -= \
                (knights[(i + 1) % 2].power - knights[i].protection)
            if knights[i].hp <= 0:
                knights[i].hp = 0

        return {knights[0].name: knights[0].hp,
                knights[1].name: knights[1].hp}
