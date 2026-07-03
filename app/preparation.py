import copy


class Preparation:

    def apply_equipment(self, knight_data: dict) -> dict:
        knight = copy.deepcopy(knight_data)

        knight["protection"] = 0

        armour = knight.get("armour") or []
        knight["protection"] += sum(a["protection"] for a in armour)

        # Apply weapon
        knight["power"] += knight["weapon"]["power"]

        # Apply potion if exists
        if knight["potion"] is not None:
            effect = knight["potion"]["effect"]
            knight["power"] += effect.get("power", 0)
            knight["protection"] += effect.get("protection", 0)
            knight["hp"] += effect.get("hp", 0)

        return knight

    def prepare_all(self, knights_dict: dict) -> dict:
        prepared_knights = {}
        for key, data in knights_dict.items():
            prepared_knights[key] = self.apply_equipment(data)
        return prepared_knights
