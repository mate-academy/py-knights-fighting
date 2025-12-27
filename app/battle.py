from app.knight import Knight


class Battle:
    """Manages battles between knights."""

    def __init__(self, knights_config: dict):
        """Initialize battle with knights configuration."""
        self.knights = self._create_knights(knights_config)

    def _create_knights(self, knights_config: dict) -> dict:
        """Create Knight objects from configuration."""
        knights = {}
        for key, config in knights_config.items():
            knights[key] = Knight(config)
        return knights

    def prepare_all_knights(self):
        """Prepare all knights for battle by applying equipment."""
        for knight in self.knights.values():
            knight.prepare_for_battle()

    def fight(self, knight1_key: str, knight2_key: str):
        """Execute a fight between two knights."""
        knight1 = self.knights[knight1_key]
        knight2 = self.knights[knight2_key]

        # Both knights attack simultaneously
        knight1.take_damage(knight2.power)
        knight2.take_damage(knight1.power)

    def get_results(self) -> dict:
        """Get battle results as dictionary with knight names and their HP."""
        return {knight.name: knight.hp for knight in self.knights.values()}
