from app.knight import Knight


def print_the_knight(knight: Knight) -> None:
    """
    This function prints characteristics of knights
    """
    print(f"""
            Knight's name: {knight.name}.
            Knight's power: {knight.power}.
            Knight's hp: {knight.hp}.
            Knight's protection: {knight.protection}
            """)
