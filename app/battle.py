from __future__ import annotations

from app.person import Person, arthur, lancelot, red_knight, mordred


def game(person: Person, other: Person) -> tuple:
    person.hp -= other.power - person.protection
    other.hp -= person.power - other.protection
    defeat(person)
    defeat(other)
    return person.hp, other.hp


def total_result() -> dict:
    result = {}
    game(lancelot, arthur)
    game(mordred, red_knight)
    result[lancelot.name] = lancelot.hp
    result[arthur.name] = arthur.hp
    result[mordred.name] = mordred.hp
    result[red_knight.name] = red_knight.hp
    return result


def defeat(person: Person) -> None:
    if person.hp <= 0:
        person.hp = 0
