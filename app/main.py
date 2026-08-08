from app.cnights_stats import KNIGHTS


def knight(knights_stats: dict, fighter: str) -> dict:
    fighter_in_dict = knights_stats[f"{fighter}"]
    fighter_in_dict["protection"] = 0
    for item in fighter_in_dict["armour"]:
        fighter_in_dict["protection"] += item["protection"]
    fighter_in_dict["power"] += fighter_in_dict["weapon"]["power"]
    if fighter_in_dict["potion"] is not None:
        if "power" in fighter_in_dict["potion"]["effect"]:
            fighter_in_dict["power"]\
                += fighter_in_dict["potion"]["effect"]["power"]
        if "protection" in fighter_in_dict["potion"]["effect"]:
            fighter_in_dict["protection"]\
                += fighter_in_dict["potion"]["effect"]["protection"]
        if "hp" in fighter_in_dict["potion"]["effect"]:
            fighter_in_dict["hp"] += fighter_in_dict["potion"]["effect"]["hp"]
    return fighter_in_dict


def check_if_someone_fell_in_battle(fighter: dict) -> None:
    if fighter["hp"] <= 0:
        fighter["hp"] = 0


def battle_process(first_fighter: dict, second_fighter: dict) -> None:
    first_fighter["hp"]\
        -= (second_fighter["power"] - first_fighter["protection"])
    second_fighter["hp"]\
        -= first_fighter["power"] - second_fighter["protection"]


def battle(knights_stats: dict) -> dict:
    lancelot = knight(knights_stats, "lancelot")
    mordred = knight(knights_stats, "mordred")
    arthur = knight(knights_stats, "arthur")
    red_knight = knight(knights_stats, "red_knight")
    fighters = [lancelot, mordred, arthur, red_knight]
    battle_process(lancelot, mordred)
    battle_process(arthur, red_knight)
    for fighter in fighters:
        check_if_someone_fell_in_battle(fighter)
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
