from app.warrior.stats import Stats


class Potion:
    def __init__(self, potion_dict: dict | None) -> None:
        if potion_dict:
            self.name = potion_dict["name"]
            self.stats = Stats(**potion_dict["effect"])
        else:
            self.name = None
            self.stats = Stats()
