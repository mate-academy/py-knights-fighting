class Knights:
    lancelot: dict
    arthur: dict
    mordred: dict
    red_knight: dict
    list_knights: list["Knights"] = []
    def __init__(self, data: dict, protection: int = 0) -> None:
        self.protection = protection
        for key, value in data.items():
            setattr(self, key, value)
            Knights.list_knights.append(getattr(self, key))

    # def __repr__(self) -> str:
    #     return f"{self}"