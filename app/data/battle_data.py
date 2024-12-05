from app.data.knight_data import KnightData


class BattleData:
    def __init__(self, knights_configs: dict):
        self.knights_data = [
            KnightData(knight_config)
            for knight_config in knights_configs.values()
        ]
