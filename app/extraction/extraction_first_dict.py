def extract_first_dict(some_dict: dict) -> dict:
    first_key, first_value = next(iter(some_dict.items()))
    new_dict = {first_key: first_value}
    return new_dict
