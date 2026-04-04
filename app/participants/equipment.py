def add_equipment(basic_participants: list, given_data: dict) -> None:

    for each_participant in basic_participants:
        participant_data = given_data[each_participant.internal_name]
        weapons = participant_data["weapon"]
        armours = participant_data["armour"]
        potion = participant_data["potion"]

        each_participant.power += weapons["power"]

        if armours:
            protection_bonus = sum(armor["protection"] for armor in armours)
            each_participant.protection += protection_bonus

        if potion:
            each_participant.hp += (
                potion["effect"].get("hp", 0))
            each_participant.power += (
                potion["effect"].get("power", 0))
            each_participant.protection += (
                potion["effect"].get("protection", 0))
