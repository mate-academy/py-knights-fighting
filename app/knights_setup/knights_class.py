from app.knights_setup.knight_class import Knight


class Knights:
    """
    The class is used to store Knight instances.
    """
    knights = dict()

    @classmethod
    def add_knight(cls, knight_name: str, knight: Knight) -> None:
        cls.knights.update({knight_name: knight})

    def __getitem__(self, item: str) -> Knight | None:
        return Knights.knights.get(item)
