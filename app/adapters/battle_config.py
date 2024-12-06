from app.adapters.knight_config import KnightConfig


class BattleConfig:
    def __init__(self, knights_configs: dict[str, dict]) -> None:
        self.knight_datas = [
            KnightConfig(knight_config)
            for knight_config in knights_configs.values()
        ]
