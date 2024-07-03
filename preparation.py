def apply_armour(knight):
    knight["protection"] = sum(a["protection"] for a in knight["armour"])


def apply_weapon(knight):
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight):
    if knight["potion"] is not None:
        for effect, value in knight["potion"]["effect"].items():
            if effect in knight:
                knight[effect] += value


def prepare_knight(knight_name):
    def decorator(func):
        def wrapper(knights_config):
            knight = knights_config[knight_name]
            apply_armour(knight)
            apply_weapon(knight)
            apply_potion(knight)
            return func(knights_config)
        return wrapper
    return decorator
