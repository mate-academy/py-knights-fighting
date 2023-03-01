def prepar(knig):

    for i in knig:
        if bool(i['armour']) is not False:
            am = len(i['armour'])
            for w in range(am):
                i['protection'] += i['armour'][w]['protection']

        i['power'] += i["weapon"]["power"]

        if i["potion"] is not None:
            if "power" in i["potion"]["effect"]:
                i["power"] += i["potion"]["effect"]["power"]
            if "protection" in i["potion"]["effect"]:
                i["protection"] += i["potion"]["effect"]["protection"]
            if "hp" in i["potion"]["effect"]:
                i["hp"] += i["potion"]["effect"]["hp"]
    return knig
