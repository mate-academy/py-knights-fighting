def fight(first_knight: dict, second_knight: dict) -> None:
    first_damage = (
        second_knight["power"]
        - first_knight["protection"]
    )
    second_damage = (
        first_knight["power"]
        - second_knight["protection"]
    )

    first_knight["hp"] -= first_damage
    second_knight["hp"] -= second_damage

    if first_knight["hp"] < 0:
        first_knight["hp"] = 0

    if second_knight["hp"] < 0:
        second_knight["hp"] = 0
