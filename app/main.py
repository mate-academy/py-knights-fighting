from app.config.logic import Preparation


def battle(config: dict) -> dict:
    attention = Preparation(config)
    return attention.start_of_tournament()
