from app.adapters.knight_config import KnightConfig


class ArenaConfig:
    """
    Used as argument for creating Arena

    Properties:
        knight_configs (list[KnightConfig]): list of KnightConfig objects
        matchups (list[tuple[str, str]]):
            names of knights that are to fight each other
    """

    def __init__(
            self,
            knights_dicts: dict[str, dict],
            matchups: list[tuple[str, str]]
    ) -> None:
        self.knight_configs = (
            KnightConfig.extract_knight_configs(knights_dicts)
        )
        self.matchups = matchups
