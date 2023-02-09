from app.buttle.models import Knight


def make_knights(knights_config: dict) -> list[Knight]:
    return Knight.make_list_of_knights(knights_config)
