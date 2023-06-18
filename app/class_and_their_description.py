class KnightCreator:

    def __init__(self, knights: dict) -> None:
        self.name = knights["name"]
        self.hp = knights["hp"]
        self.power = knights["power"]
        self.protection = 0

    def __str__(self) -> str:
        return f"name: {self.name}, " \
               f"hp: {self.hp}, " \
               f"power: {self.power}, " \
               f"protection: {self.protection}"

    def upgrading_knight(self, stats: dict) -> "KnightCreator":
        self.power += stats["weapon"].get("power")
        self.protection += sum(
            [
                protect["protection"]
                for protect in stats["armour"]
            ]
        )

        if stats["potion"] is not None:
            self.hp += stats["potion"].get("effect").get("hp", 0)
            self.power += stats["potion"].get("effect").get("power", 0)
            self.protection += \
                stats["potion"].get("effect").get("protection", 0)

        return self

    @staticmethod
    def duel(
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
