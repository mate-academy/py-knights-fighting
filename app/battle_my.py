from app.class_knight import Knight


def one_on_one(first_knight: str, second_knight: str) -> dict:
    result = {}
    Knight.list_knight[first_knight].hp -= \
        (Knight.list_knight[second_knight].power
         - Knight.list_knight[first_knight].armour)
    Knight.list_knight[second_knight].hp -= \
        (Knight.list_knight[first_knight].power
            - Knight.list_knight[second_knight].armour)
    if Knight.list_knight[first_knight].hp <= 0:
        Knight.list_knight[first_knight].hp = 0
    if Knight.list_knight[second_knight].hp <= 0:
        Knight.list_knight[second_knight].hp = 0
    result[Knight.list_knight[first_knight].name] = (
        Knight.list_knight[first_knight].hp)
    result[Knight.list_knight[second_knight].name] = (
        Knight.list_knight[second_knight].hp)
    return result
