from app.apply.armour import apply_armour
from app.apply.point import apply_point


def apply_all(name: dict) -> None:
    apply_armour(name)
    name["power"] += name["weapon"]["power"]
    apply_point(name)
