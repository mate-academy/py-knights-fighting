from app.heroes.battle import KNIGHTS


def prepare_knight(knight: dict) -> None:
    """Preparing knights"""
    knight["protection"] = sum(
        armor["protection"] for armor in knight["armour"]
    )
    knight["power"] += knight["weapon"]["power"]

    potion = knight.get("potion")
    if potion:
        effect = potion.get("effect", {})
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)
        knight["hp"] += effect.get("hp", 0)


def duel(knight1: dict, knight2: dict) -> None:
    """Duel"""
    knight1["hp"] -= max(0, knight2["power"] - knight1["protection"])
    knight2["hp"] -= max(0, knight1["power"] - knight2["protection"])

    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])


def battle(knightsconfig: dict) -> dict:
    # Knights
    for name in ["lancelot", "arthur", "mordred", "red_knight"]:
        prepare_knight(knightsconfig[name])

    # Duel
    duel(knightsconfig["lancelot"], knightsconfig["mordred"])
    duel(knightsconfig["arthur"], knightsconfig["red_knight"])

    # Result
    return {
        knightsconfig["lancelot"]["name"]: knightsconfig["lancelot"]["hp"],
        knightsconfig["arthur"]["name"]: knightsconfig["arthur"]["hp"],
        knightsconfig["mordred"]["name"]: knightsconfig["mordred"]["hp"],
        knightsconfig["red_knight"]["name"]: knightsconfig["red_knight"]["hp"],
    }


print(battle(KNIGHTS))
print(KNIGHTS)
