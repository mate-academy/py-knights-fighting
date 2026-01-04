class KnightCreator:

    def __init__(self, knights: dict) -> None:
        self.name = knights["name"]
        self.hp = knights["hp"]
        self.power = knights["power"]
        self.protection = 0
        self.potion = knights["potion"]

    def __str__(self) -> str:
        return (
            f"name: {self.name},"
            f"hp: {self.hp},"
            f"power: {self.power},"
            f"protection: {self.protection}"
        )

    def upgrading_knight_before_battle(self, stats: dict) -> "KnightCreator":
        self.power += stats["weapon"].get("power")
        self.protection += sum(
            [
                protect["protection"]
                for protect in stats["armour"]
            ]
        )

        if self.potion is not None:
            for effect, value in self.potion["effect"].items():
                setattr(self, effect, getattr(self, effect, 0) + value)

        return self

    @staticmethod
    def battle_rules(
            first_knight: "KnightCreator",
            second_knight: "KnightCreator"
    ) -> dict:

        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection

        if first_knight.hp < 0:
            first_knight.hp = 0
        if second_knight.hp < 0:
            second_knight.hp = 0

        return {
            first_knight.name: first_knight.hp,
            second_knight.name: second_knight.hp
        }
