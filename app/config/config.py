from .knight1 import knight as lancelot
from .knight2 import knight as arthur
from .knight3 import knight as mordred
from .knight4 import knight as red_knight

knights = {
    "lancelot": lancelot,
    "arthur": arthur,
    "mordred": mordred,
    "red_knight": red_knight
}

battle_queue = (("lancelot", "mordred"), ("arthur", "red_knight"))
