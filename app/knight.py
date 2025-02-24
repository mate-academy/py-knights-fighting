def calculate_stats(knight: dict) -> dict:
    """
    Вычисляет эффективные характеристики рыцаря.
    Возвращает словарь с ключами: name, hp, power, protection.
    """
    effective_hp = knight["hp"]
    effective_power = knight["power"] + knight["weapon"]["power"]
    effective_protection = sum(
        item.get("protection", 0) for item in knight.get("armour", [])
    )

    potion = knight.get("potion")
    if potion is not None:
        effect = potion.get("effect", {})
        effective_hp += effect.get("hp", 0)
        effective_power += effect.get("power", 0)
        effective_protection += effect.get("protection", 0)

    return {
        "name": knight["name"],
        "hp": effective_hp,
        "power": effective_power,
        "protection": effective_protection,
    }
