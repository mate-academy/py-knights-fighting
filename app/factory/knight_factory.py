from typing import List

from app.config.knight_config import KnightConfig
from app.entities.knight import Knight


class KnightFactory:
    def __init__(self, knights_data: dict) -> None:
        """
        Initializes the factory with raw knight configuration data. The data
        contains stats and equipment definitions that will be transformed
        into fully prepared Knight instances.

        :param knights_data: dict with raw knight configs keyed by names
        """
        self.knights_data = knights_data

    def create_one_knight(self, key: str) -> Knight:
        """
        Creates a single Knight instance from config using the provided key.
        The raw data is converted to KnightConfig, prepared, and then wrapped
        into a Knight entity.

        :param key: str - key identifying a knight configuration
        :return: Knight - fully prepared knight instance
        """
        raw_data = self.knights_data.get(key)
        config = KnightConfig(raw_data)
        config.prepare()
        return Knight(config)

    def create_all_knights(self) -> List[Knight]:
        """
        Creates Knight instances for all configurations passed into the
        factory. Each knight is processed, prepared and returned as a list.

        :return: List[Knight] - all prepared knight instances
        """
        return [self.create_one_knight(key=key) for key in self.knights_data]
