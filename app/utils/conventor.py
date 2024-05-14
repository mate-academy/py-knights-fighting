from __future__ import annotations
from app.models.knight import Knight


def convertor(knights_dict: dict) -> dict:
    knights = {
        knight_data["name"]: Knight(**knight_data)
        for knight_data in knights_dict.values()
    }
    return knights
