from app.service.make_knight import make_knight


def make_knights(knights: dict) -> dict:
    return {knight_name: make_knight(knight_body)
            for knight_name, knight_body in knights.items()}
