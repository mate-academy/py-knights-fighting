from app.knights import Knight


class Battle:

    knights = []

    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight
        self.knights.extend([first_knight, second_knight])

    def check_someone_fell(self) -> None:
        died = "was mortally wounded and died"
        if self.first_knight.is_died():
            print(f"{self.first_knight.name} {died}")
        elif self.second_knight.is_died():
            print(f"{self.second_knight.name} {died}")
        else:
            print("Both knights survived the battle")

    @classmethod
    def before_start(cls) -> None:
        for knight in cls.knights:
            knight.upgrade_stats()

    def start_battle(self) -> None:
        print(f"Let's start the battle between {self.first_knight.name}"
              f" and {self.second_knight.name}!")
        self.first_knight.hp -= (
            self.second_knight.power - self.first_knight.protection
        )
        self.second_knight.hp -= (
            self.first_knight.power - self.second_knight.protection)
        self.check_someone_fell()

    @classmethod
    def battles_result(cls) -> dict:
        return {knight.name: knight.hp for knight in cls.knights}
