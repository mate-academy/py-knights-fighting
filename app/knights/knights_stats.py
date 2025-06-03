class Knight:

    def __init__(self, stats: dict) -> None:
        for key, value in stats.items():
            setattr(self, key, value)


if __name__ == "__main__":
    pass
