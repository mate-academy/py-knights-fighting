class Win:

    @staticmethod
    def result_of_tournament(kings: dict) -> dict:
        return {x : y["hp"] for x, y in kings.items()}
