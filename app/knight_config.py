from typing import Dict, List, Union


Knight_Config = Dict[
    str,
    Union[
        str,
        int,
        List[Dict[str, Union[str, int]]],
        Dict[str, Union[str, int, Dict[str, int]]]
    ]
]
