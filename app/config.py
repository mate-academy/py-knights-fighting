from app.game.models import Knight, Weapon, Armour, Potion

KNIGHTS = {
    "lancelot": Knight(
        name="Lancelot",
        power=50,
        hp=100,
        armour=[Armour(part="helmet", protection=10)],
        weapon=Weapon(name="Sword", power=40),
        potion=Potion(
            name="Strength Elixir",
            effect={"hp": 10, "power": 5, "protection": 5}
        ),
    ),
    "mordred": Knight(
        name="Mordred",
        power=55,
        hp=90,
        armour=[Armour(part="shield", protection=15)],
        weapon=Weapon(name="Axe", power=50),
        potion=None,
    ),
}