def action(knights_dict: dict) -> dict:
    knights_dict["lancelot"]["hp"] -= \
        knights_dict["mordred"]["power"] -\
        knights_dict["lancelot"]["protection"]
    knights_dict["mordred"]["hp"] -= \
        knights_dict["lancelot"]["power"] -\
        knights_dict["mordred"]["protection"]
    knights_dict["arthur"]["hp"] -= \
        knights_dict["red_knight"]["power"] -\
        knights_dict["arthur"]["protection"]
    knights_dict["red_knight"]["hp"] -= \
        knights_dict["arthur"]["power"] -\
        knights_dict["red_knight"]["protection"]
    return knights_dict
