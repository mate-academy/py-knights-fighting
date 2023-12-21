class KingsConfigur:

    def __init__(self, king_list: dict) -> None:
        self.king_list = king_list

    def configure(self) -> dict:
        new_result = {}
        for i in self.king_list:
            king_configur = self.king_list[i]

            # apply armour
            king_configur["protection"] = 0
            for element in king_configur["armour"]:
                king_configur["protection"] += element["protection"]

            # apply weapon
            king_configur["power"] += king_configur["weapon"]["power"]

            # apply potion if exist
            if king_configur["potion"] is not None:
                if "power" in king_configur["potion"]["effect"]:
                    king_configur["power"] += (
                        king_configur)["potion"]["effect"]["power"]

                if "protection" in king_configur["potion"]["effect"]:
                    king_configur["protection"] += (
                        king_configur)["potion"]["effect"]["protection"]

                if "hp" in king_configur["potion"]["effect"]:
                    king_configur["hp"] += (
                        king_configur)["potion"]["effect"]["hp"]

            new_result[king_configur["name"]] = king_configur

        return new_result
