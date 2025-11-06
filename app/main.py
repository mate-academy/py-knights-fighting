from typing import cast

from app.knight.knight import Knight, implement_knights_and_stuff
from app.knight.knights_data import KNIGHTS


def battle(knights: dict) -> dict:
    lancelot = cast(
        Knight, implement_knights_and_stuff("lancelot", knights)
    )
    arthur = cast(
        Knight, implement_knights_and_stuff("arthur", knights)
    )
    mordred = cast(
        Knight, implement_knights_and_stuff("mordred", knights)
    )
    red_knight = cast(
        Knight, implement_knights_and_stuff("red_knight", knights)
    )

    return {
        lancelot.name: lancelot.count_hp(mordred),
        mordred.name: mordred.count_hp(lancelot),
        arthur.name: arthur.count_hp(red_knight),
        red_knight.name: red_knight.count_hp(arthur),
    }


print(battle(KNIGHTS))
