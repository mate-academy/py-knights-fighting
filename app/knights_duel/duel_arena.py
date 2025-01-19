class DuelArena:
    @staticmethod
    def ready_up(knight: dict) -> dict:
        result = {
            "name": knight["name"],
            "power": knight["power"] + knight["weapon"]["power"],
            "hp": knight["hp"],
            "protection": 0,
        }

        for armour in knight["armour"]:
            result["protection"] += armour["protection"]

        if knight["potion"] is not None:
            result["power"] += knight["potion"]["effect"].get("power", 0)
            result["hp"] += knight["potion"]["effect"].get("hp", 0)
            result["protection"] += (
                knight["potion"]["effect"].get("protection", 0)
            )

        return result

    @staticmethod
    def battle_knights(first_knight: dict, second_knight: dict) -> int:
        hp_first_knight = (
            first_knight["hp"]
            + first_knight["protection"]
            - second_knight["power"]
        )

        return hp_first_knight if hp_first_knight > 0 else 0
