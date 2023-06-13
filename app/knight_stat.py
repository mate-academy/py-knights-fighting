def calculate_knight_stats(curr_knight: dict) -> dict:
    curr_knight["protection"] = 0
    for part in curr_knight["armour"]:
        curr_knight["protection"] += part["protection"]

    curr_knight["power"] += curr_knight["weapon"]["power"]

    if curr_knight["potion"] is not None:
        stat_list = ["power", "protection", "hp"]
        for stat in stat_list:
            if stat in curr_knight["potion"]["effect"]:
                curr_knight[stat] += curr_knight["potion"]["effect"][stat]

    return {
        "name": curr_knight["name"],
        "hp": curr_knight["hp"],
        "power": curr_knight["power"],
        "protection": curr_knight["protection"]
    }



curr_knight = {
    "name": "Arthur",
    "power": 45,
    "hp": 75,
    "armour": [
        {
            "part": "helmet",
            "protection": 15,
        },
        {
            "part": "breastplate",
            "protection": 20,
        },
        {
            "part": "boots",
            "protection": 10,
        }
    ],
    "weapon": {
        "name": "Two-handed Sword",
        "power": 55,
    },
    "potion": None,
}


knight_stats = calculate_knight_stats(curr_knight)


print(knight_stats)