class Battle:

    result = {}

    def __init__(
            self,
            one_knight: dict,
            two_knight: dict,
    ) -> None:

        self.one_knight = one_knight
        self.two_knight = two_knight

    def battle_knight(self) -> dict:

        self.one_knight["hp"] -= \
            self.two_knight["power"] - self.one_knight["protection"]
        self.two_knight["hp"] -= \
            self.one_knight["power"] - self.two_knight["protection"]

        if self.one_knight["hp"] <= 0:
            self.one_knight["hp"] = 0

        if self.two_knight["hp"] <= 0:
            self.two_knight["hp"] = 0

        Battle.result[self.one_knight["name"]] = self.one_knight["hp"]
        Battle.result[self.two_knight["name"]] = self.two_knight["hp"]

        return Battle.result
