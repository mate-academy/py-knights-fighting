from app.knights_change.knights import Knights


def add_armor(knight: "Knights") -> None:
    knight.protection = sum(piece.protection for piece in knight.armour)


def add_weapon(knight: "Knights") -> None:
    knight.power += knight.weapon.power


def add_potion(knight: "Knights") -> None:
    if knight.potion is not None:
        knight.power += knight.potion.power
        knight.protection += knight.potion.protection
        knight.hp += knight.potion.hp


def get_ready(knight: "Knights") -> None:
    add_weapon(knight)
    add_armor(knight)
    add_potion(knight)
