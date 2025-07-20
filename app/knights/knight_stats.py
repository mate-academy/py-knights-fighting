class Knight:

    def __init__(self, name: str, power: int,
                 hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def equip_armour(self, armour: list) -> None:
        for armour_piece in armour:
            self.protection += armour_piece.get("protection", 0)

    def equip_weapon(self, weapon: dict) -> None:
        self.power += weapon.get("power", 0)

    def use_potion(self, potion: dict) -> None:
        effect = potion.get("effect", {})
        self.power += effect.get("power", 0)
        self.hp += effect.get("hp", 0)
        self.protection += effect.get("protection", 0)

    @staticmethod
    def prepare(knights: dict) -> list:
        knights_dicts_list = list(knights.values())
        prepared_knights = [
            Knight(knight.get("name", "John Doe"),
                   knight.get("power", 0),
                   knight.get("hp", 0))
            for knight in knights_dicts_list]

        for knight, data in zip(prepared_knights, knights_dicts_list):
            (knight.equip_armour(data.get("armour")))
            (knight.equip_weapon(data.get("weapon")))
            if data.get("potion", None):
                (knight.use_potion(data.get("potion")))

        return prepared_knights
