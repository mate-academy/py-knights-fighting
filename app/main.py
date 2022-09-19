from app.config.config import Preparation


def battle(config: dict) -> dict:
    attention = Preparation(config)
    return attention.start_of_tournament()
