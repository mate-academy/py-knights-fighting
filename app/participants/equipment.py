def add_equipment(basic_participants: list, given_data: dict) -> None:

    for each_participant in basic_participants:

        weapons = given_data[each_participant.internal_name]["weapon"]
        armours = given_data[each_participant.internal_name]["armour"]
        potion = given_data[each_participant.internal_name]["potion"]

        each_participant.power += weapons["power"]
        if armours:
            for each_armor in armours:
                each_participant.protection += each_armor["protection"]

        if potion:
            each_participant.hp += (
                potion["effect"].get("hp", 0))
            each_participant.power += (
                potion["effect"].get("power", 0))
            each_participant.protection += (
                potion["effect"].get("protection", 0))
