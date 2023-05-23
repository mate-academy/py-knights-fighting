class Item:
    """
    Represents an item in knights inventory;
    item_kind : can be either "equip" or "use", on which depends
    when knight will have benefits from it;
    name: stores name of item in inventory
    stats: a list of stat modifiers the item bears, should be stored in dict
    in form like stat_name":"stat_modifier
    """

    def __init__(self, item_kind: str, name: str, stats: list) -> None:
        self.item_kind = item_kind
        self.name = name
        self.stats = stats

    def __repr__(self) -> str:
        return (f"{self.item_kind} this {self.name} "
                f"to get such effects: {self.stats}")
