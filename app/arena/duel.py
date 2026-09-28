from app.knights import Knight


def duel(first: Knight, second: Knight) -> None:
    first.take_hit(second)
    second.take_hit(first)
