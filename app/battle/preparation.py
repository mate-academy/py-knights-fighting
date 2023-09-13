from app.Challengers.Knight import Hero


class PreparedKnights:

    @staticmethod
    def knights_to_dict(knight_data: dict) -> dict:
        """Create a list of Hero instances from a knights_data dictionary."""
        return {data["name"]: Hero(
            data["name"], data["power"], data["hp"]
        ) for data in knight_data.values()
        }

    @staticmethod
    def prepare_knights(
            knights_to_dict: dict,
            knights_data: dict
    ) -> dict:
        """
        Changes Hero instances of all_knights list
        with data from knights_data dictionary.
        """
        for fighter in knights_data.values():
            fighter["armour"] = sum(
                part["protection"] for part in fighter["armour"]
            )
            fighter["power"] += fighter["weapon"]["power"]

            if fighter["potion"]:
                potion_effect = fighter["potion"]["effect"]
                fighter["power"] += potion_effect.get("power", 0)
                fighter["hp"] += potion_effect.get("hp", 0)
                fighter["armour"] += potion_effect.get("protection", 0)

        for knight in knights_to_dict.values():
            for data in knights_data.values():
                if knight.name == data["name"]:
                    knight.armour = data["armour"]
                    knight.power = data["power"]
                    knight.hp = data["hp"]

        return knights_to_dict
