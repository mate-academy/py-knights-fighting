class Result:
    result = {}

    @staticmethod
    def show_result(knights):
        Result.result = ({knight.name: knight.hp for knight in knights})
        return Result
