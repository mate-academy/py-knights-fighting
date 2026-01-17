class KingsConfigur:

    def __init__(self, kings: dict) -> None:
        self.kings = kings

    def configure(self) -> dict:
        new_result = {}
        for king in self.kings:
            king_configur = self.kings[king]

            # apply armour
            king_configur["protection"] = 0
            for element in king_configur["armour"]:
                king_configur["protection"] += element["protection"]

            # apply weapon
            king_configur["power"] += king_configur["weapon"]["power"]

            # apply potion if exist
            if king_configur["potion"] is not None:
                for elements in king_configur["potion"]["effect"]:
                    king_configur[elements] += (
                        king_configur)["potion"]["effect"][elements]

            new_result[king_configur["name"]] = king_configur

        return new_result
