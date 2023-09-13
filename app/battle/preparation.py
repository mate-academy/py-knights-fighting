from app.Challengers.Knight import Hero


class PreparedKnights:

    @staticmethod
    def list_knights(knight_data: dict) -> list[Hero]:
        """Create a list of Hero instances from a knights_data dictionary."""
        return [
            Hero(
                knight_data[data]["name"],
                knight_data[data]["power"],
                knight_data[data]["hp"]) for data in knight_data
        ]

    @staticmethod
    def prepare_knights(
            list_knights: list[Hero],
            knights_data: dict
    ) -> list[Hero]:
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

        for knight in list_knights:
            for data in knights_data.values():
                if knight.name == data["name"]:
                    knight.armour = data["armour"]
                    knight.power = data["power"]
                    knight.hp = data["hp"]

        return list_knights
