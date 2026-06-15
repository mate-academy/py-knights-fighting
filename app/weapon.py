def weapon(knights_dict: dict) -> None:
    for key, knight in knights_dict.items():
        knight["power"] += knight["weapon"]["power"]
