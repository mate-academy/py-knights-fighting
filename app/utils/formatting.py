def list_to_string(items: list) -> str:
    return ', '.join(str(item) for item in items)


def number_to_string(number: int | float) -> str:
    if number > 0:
        return "+" + str(number)
    return str(number)


def number_as_bar(number, min_value=0, max_value=100, bars=10) -> str:
    number = max(
        min_value,
        min(number, max_value)
    )
    return ("||" * (number // bars)) + ("  " * (bars - number // bars))