def ready_to_battle(knights: dict) -> list[tuple]:
    knights_ready = []
    for knight in knights:
        name = knights[knight]["name"]
        hp = knights[knight]["hp"]
        power = knights[knight]["power"]
        protection = 0

        for armour in knights[knight]["armour"]:
            protection += armour["protection"]

        power += knights[knight]["weapon"]["power"]

        if knights[knight]["potion"] is not None:
            if "power" in knights[knight]["potion"]["effect"]:
                power += knights[knight]["potion"]["effect"]["power"]

            if "protection" in knights[knight]["potion"]["effect"]:
                protection += knights[knight]["potion"]["effect"]["protection"]

            if "hp" in knights[knight]["potion"]["effect"]:
                hp += knights[knight]["potion"]["effect"]["hp"]
        knights_ready.append((name, hp, protection, power))
    return knights_ready
