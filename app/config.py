from app.models import Knight, Weapon, Armour, Potion

KNIGHTS = {
    "lancelot": Knight(
        name="Lancelot",
        base_power=50,
        base_hp=80,
        armour=[Armour("helmet", 15), Armour("breastplate", 30)],
        weapon=Weapon("Lance", 60),
        potion=Potion("Courage Brew", {"hp": +10, "power": +5}),
    ),
    "mordred": Knight(
        name="Mordred",
        base_power=55,
        base_hp=85,
        armour=[Armour("shield", 20)],
        weapon=Weapon("Dark Sword", 50),
        potion=None,
    ),
    "arthur": Knight(
        name="Arthur",
        base_power=60,
        base_hp=90,
        armour=[Armour("breastplate", 25)],
        weapon=Weapon("Excalibur", 70),
        potion=Potion("Strength Elixir", {"hp": +15, "power": +10}),
    ),
    "red_knight": Knight(
        name="Red Knight",
        base_power=40,
        base_hp=70,
        armour=[Armour("breastplate", 25)],
        weapon=Weapon("Sword", 45),
        potion=Potion("Blessing", {"hp": +10, "power": +5}),
    ),
}
