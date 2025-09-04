from app.models.Knight import Knight
from app.data.knight_data import KNIGHTS
import copy

def prepare_knights(knights_data: dict) -> dict:
    prepared = {}
    for key, data in knights_data.items():
        data_copy = copy.deepcopy(data)
        knight = Knight.from_dict(data_copy)   # створюємо об'єкт Knight
        knight.apply_potion_effects()         # застосовуємо броню, зброю та зілля
        prepared[key] = knight
    return prepared

if __name__ == "__main__":
    prepared = prepare_knights(KNIGHTS)
    for k, knight in prepared.items():
        print(knight)