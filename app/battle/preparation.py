from app.challengers.Knight import Hero


class PreparedKnights:

    @staticmethod
    def knights_to_dict(knight_data: dict) -> dict:
        return {data["name"]: Hero(
            data["name"], data["power"], data["hp"]
        ) for data in knight_data.values()
        }

    @staticmethod
    def prepare_knights(
            dict_of_knights: dict,
            knights_data: dict
    ) -> dict:

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

        for knight in dict_of_knights.values():
            for data in knights_data.values():
                if knight.name == data["name"]:
                    knight.armour = data["armour"]
                    knight.power = data["power"]
                    knight.hp = data["hp"]

        return dict_of_knights