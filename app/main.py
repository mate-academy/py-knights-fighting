from knights_configuration.configurator import Configurator


def battle(knights: dict) -> dict:
    config = Configurator(knights)
    return config.battle()
