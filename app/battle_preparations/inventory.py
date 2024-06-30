class Inventory:
    @staticmethod
    def apply_armour(armour: list[dict]) -> int:
        protection = 0
        for armour_unit in armour:
            protection += armour_unit["protection"]
        return protection

    @staticmethod
    def apply_weapon(init_power: int, weapon: dict) -> int:
        return init_power + weapon["power"]

    @staticmethod
    def apply_potion(knight: dict) -> dict:
        relevant_stats = ["power", "protection", "hp"]
        if knight["potion"] is not None:
            for stat in relevant_stats:
                if stat in knight["potion"]["effect"]:
                    knight[stat] += knight["potion"]["effect"][stat]

        return knight
