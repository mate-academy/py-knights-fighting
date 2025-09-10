from __future__ import annotations

from app.entity.knights import Knights


class Arena:

    @staticmethod
    def duel(fighter_one: Knights, fighter_two: Knights) -> None:
        fighter_one.health -= fighter_two.power - fighter_one.protection
        fighter_two.health -= fighter_one.power - fighter_two.protection

    @staticmethod
    def is_lose(fighter: Knights) -> None:
        if fighter.health <= 0:
            fighter.health = 0

    @staticmethod
    def fight(fighter_one: Knights, fighter_two: Knights) -> None:
        Arena.duel(fighter_one, fighter_two)
        Arena.is_lose(fighter_one)
        Arena.is_lose(fighter_two)
