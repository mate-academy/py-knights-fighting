
def validate_knight_config(key: str, data: dict) -> None:
    if "name" not in data:
        raise ValueError(f"Knight {key} must have a name")
