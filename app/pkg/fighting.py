from app.pkg.class_knights import Knight


def fighting(first: str, second: str, knights_dict: dict) -> None:

    knights_dict[first].hp -= knights_dict[second].power \
        - knights_dict[first].protection
    knights_dict[second].hp -= knights_dict[first].power \
        - knights_dict[second].protection

    knights_dict[first].hp = Knight.check_hp_knight(knights_dict[first].hp)
    knights_dict[second].hp = Knight.check_hp_knight(knights_dict[second].hp)
