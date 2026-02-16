from app.data.loadouts import (
    lancelot_loadout,
    arthur_loadout,
    mordred_loadout,
    red_knight_loadout
)
from app.data.default_registry import registry
from app.domain.knight import Knight

lancelot = Knight(
    name="Lancelot",
    hp=100,
    power=35,
    protection=0,
    registry=registry,
    equipment=lancelot_loadout
)

arthur = Knight(
    name="Arthur",
    hp=75,
    power=45,
    protection=0,
    registry=registry,
    equipment=arthur_loadout
)

mordred = Knight(
    name="Mordred",
    hp=90,
    power=30,
    protection=0,
    registry=registry,
    equipment=mordred_loadout
)

red_knight = Knight(
    name="Red Knight",
    hp=70,
    power=40,
    protection=0,
    registry=registry,
    equipment=red_knight_loadout
)
