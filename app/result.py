from app.knight import Knight


class Result:
    @classmethod
    def return_result(cls, knights: list[Knight]):
        result = {knight.name: knight.hp for knight in knights}
        return result
