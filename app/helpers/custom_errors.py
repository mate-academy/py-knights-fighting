class MaxLevelError(ValueError):
    def __init__(self, level: int) -> None:
        super().__init__(f"{level} is a maximum")
