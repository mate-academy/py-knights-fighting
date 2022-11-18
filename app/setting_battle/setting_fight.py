def setting_battle(first, second):
    first["hp"] -= second["power"] - first["protection"]
    second["hp"] -= first["power"] - second["protection"]

    first["hp"] = max(first["hp"], 0)
    second["hp"] = max(second["hp"], 0)

    return {
        first["name"]: first["hp"],
        second["name"]: second["hp"]
    }
