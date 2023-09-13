from app.challengers.Knight import Hero


class PreparedKnights:

    @staticmethod
    def knights_to_dict(knight_data: dict) -> dict:
        return {data["name"]: Hero(
            data["name"], data["power"], data["hp"]
        ) for data in knight_data.values()
        }
