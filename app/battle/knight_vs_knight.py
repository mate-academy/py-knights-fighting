def knight_vs_knight(knight_one: dict, knight_two: dict) -> None:
    knight_one["hp"] -= knight_two["power"] - knight_one["protection"]
    knight_two["hp"] -= knight_one["power"] - knight_two["protection"]
