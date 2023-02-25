from app.dictionary_of_knights import KNIGHTS
from app.knights import CreateKnights


def create_knights(dict_of_knights: dict) -> list[object]:
    list_of_objects = []
    new_dict = {}
    for value in dict_of_knights.values():
        total_power = []
        total_protection = []
        total_hp = []
        total_power.append(value["power"])
        total_power.append(value["weapon"].get("power"))
        total_hp.append(value["hp"])
        for knight_armors in value["armour"]:
            total_protection.append(knight_armors["protection"])
        if value["potion"] is not None:
            total_hp.append(value["potion"]["effect"]["hp"])
            total_power.append(value["potion"]["effect"]["power"])
            total_protection.append(value["potion"]
                                    ["effect"].get("protection", 0))
        new_dict["power"] = sum(total_power)
        new_dict["protection"] = sum(total_protection)
        new_dict["hp"] = sum(total_hp)
        list_of_objects.append(CreateKnights(value["name"],
                                             new_dict["power"],
                                             new_dict["protection"],
                                             new_dict["hp"]))
    # print(list_of_objects[0].__dict__)
    # print(list_of_objects[1].__dict__)
    # print(list_of_objects[2].__dict__)
    # print(list_of_objects[3].__dict__)
    return list_of_objects

# create_knights(KNIGHTS)
