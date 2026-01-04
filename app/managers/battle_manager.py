from app.models.knight import Knight


class BattleManager:
    """
    Class to manage battles between knights.

    Attributes:
        knights (dict[str, Knight]): Dictionary of all knights
    """

    def __init__(self, knights_config: dict) -> None:
        self.knights = {
            name: Knight(config)
            for name, config in knights_config.items()
        }

    def conduct_battle(self) -> dict:
        """
        Conduct the entire battle.

        Returns:
            dict[str, int]: Battle results {knight_name: remaining_health}
        """
        self._prepare_all_knights()
        self._conduct_all_fights()

        return {
            knight.name: knight.hp
            for knight in self.knights.values()
        }

    def _prepare_all_knights(self) -> None:
        """Prepare all knights for battle."""
        for knight in self.knights.values():
            knight.prepare_for_battle()

    def _conduct_all_fights(self) -> None:
        """Conduct all pairwise battles"""
        battles = (
            ("lancelot", "mordred"),
            ("arthur", "red_knight")
        )

        for knight1_id, knight2_id in battles:
            self._conduct_single_fight(knight1_id, knight2_id)

    def _conduct_single_fight(self, knight1_id: str, knight2_id: str) -> None:
        """
        Conduct a battle between two specific knights.

        Args:
            knight1_id (str): Identifier of the first knight
            knight2_id (str): Identifier of the second knight
        """
        knight1 = self.knights[knight1_id]
        knight2 = self.knights[knight2_id]

        knight1.take_damage(knight2.power)
        knight2.take_damage(knight1.power)
