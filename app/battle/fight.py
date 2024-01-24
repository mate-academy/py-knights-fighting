def fight(name_1: dict, name_2: dict) -> None:
    name_1["hp"] -= name_2["power"] - name_1["protection"]
    name_2["hp"] -= name_1["power"] - name_2["protection"]
