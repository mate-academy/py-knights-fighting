class Knight:
    def __init__(self, people: dict) -> None:
        self.people = people

    def preparing(self) -> dict:
        result_of_preparing = {}
        for name, data in self.people.items():
            self.apply_protection(data)
            data["power"] += data["weapon"]["power"]
            self.apply_potion(data)
            result_of_preparing.update({
                name: {
                    "hp": data["hp"],
                    "power": data["power"],
                    "protection": data["protection"],
                    "name": data["name"]
                }
            })
        return result_of_preparing

    @staticmethod
    def apply_protection(data: dict) -> None:
        data["protection"] = 0
        for value in data["armour"]:
            data["protection"] += value["protection"]

    @staticmethod
    def apply_potion(data: dict) -> None:
        if data["potion"] is not None:
            for effect, new_value in data["potion"]["effect"].items():
                data[effect] += new_value
