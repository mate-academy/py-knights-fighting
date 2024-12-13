from datetime import date

from app.people.knight import Knight
from app.kingdom.contest import Contest


class Kingdom:
    def __init__(self, name: str, gold: int, armed_people: dict) -> None:
        self.name = name
        self.gold = gold
        self.armed_people = armed_people
        self.knights = dict()
        print(f"The Kingdom of King {self.name} was established."
              f" It has {len(armed_people)} people and {gold} gold.")

    def create_knights(self) -> None:
        for man in self.armed_people:
            self.knights[man] = Knight(
                self.armed_people[man]["name"],
                self.armed_people[man]["power"],
                self.armed_people[man]["hp"],
                self.armed_people[man]["armour"],
                self.armed_people[man]["weapon"],
                self.armed_people[man]["potion"]
            )

    def create_contest(self) -> Contest:
        return Contest(date.today(), self.name, self.knights)
