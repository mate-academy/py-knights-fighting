class Knight:
    def __init__(self, persons: dict) -> None:
        self.persons = persons

    def preparing(self: dict) -> dict:
        result_of_preparing = {}
        for name, data in self.items():
            data["protection"] = 0
            for value in data["armour"]:
                data["protection"] += value["protection"]
            data["power"] += data["weapon"]["power"]
            ls = ["power", "protection", "hp"]
            if data["potion"] is not None:
                for new_value in ls:
                    if new_value in data["potion"]["effect"]:
                        data[new_value] += data["potion"]["effect"][new_value]
            result_of_preparing.update({
                name: {"hp": data["hp"],
                       "power": data["power"],
                       "protection": data["protection"]}})
        return result_of_preparing
