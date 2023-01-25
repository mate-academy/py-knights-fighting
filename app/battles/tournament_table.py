class Table:
    @staticmethod
    def results(participants: dict) -> dict:
        return {
            knight_name: knight.health
            for knight_name, knight in participants.items()
        }
