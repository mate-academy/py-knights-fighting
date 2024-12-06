from app.adapters.knight_adapter import KnightAdapter


class BattleAdapter:
    def __init__(self, knights_configs: dict[str, dict]) -> None:
        self.knight_datas = [
            KnightAdapter(knight_config)
            for knight_config in knights_configs.values()
        ]
