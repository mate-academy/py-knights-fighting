from app.skil.factory import build_knight
from app.skil.model import Knight


def build_knights(knights: dict[str, dict]) -> dict[str, Knight]:
    result = {}
    for key, value in knights.items():
        inst = build_knight(value)
        inst.prepare()
        result[key] = inst

    return result
