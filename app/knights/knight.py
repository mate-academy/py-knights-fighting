from dataclasses import dataclass
from app.knights.data import knights_attr

@dataclass
class Knight(knights_attr):
    def __init__(self) -> None:
