from app.warrior.knight import Knight
from app.arena.arena_errors import MissingWarriorError


class Arena:
    def __init__(self, warriors: dict[str, Knight], duels: tuple) -> None:
        self.warriors = warriors or {}
        self.duels = duels

    def battle(self) -> dict:
        for duel in self.duels:
            for name in duel:
                if name not in self.warriors:
                    raise MissingWarriorError(
                        f"{name} is not in the fighter's list"
                    )

            first_name, second_name = duel
            first = self.warriors[first_name]
            second = self.warriors[second_name]

            damage_to_first = max(0, second.power - first.protection)
            damage_to_second = max(0, first.power - second.protection)

            first.hp = max(0, first.hp - damage_to_first)
            second.hp = max(0, second.hp - damage_to_second)

        return {
            name: warrior.hp
            for name, warrior in self.warriors.items()
        }
