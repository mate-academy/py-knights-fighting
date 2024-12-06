from app.adapters.inventory_config import InventoryConfig


class KnightConfig:
    def __init__(self, knight_config: dict[str, str | int | dict]) -> None:
        self.name = str(knight_config.get("name", None))
        self.power = int(knight_config.get("power", 0))
        self.hp = int(knight_config.get("hp", 0))
        self.protection = int(knight_config.get("protection", 0))

        self.inventory_data = InventoryConfig(knight_config)
