from app.knight import Knight
from app.items import Weapon, Armour, Potion


def battle(knightsconfig: dict) -> dict:
    lancelot = Knight(
        name="Lancelot",
        power=knightsconfig["lancelot"]["power"],
        hp=knightsconfig["lancelot"]["hp"],
        weapon=Weapon(
            name=knightsconfig["lancelot"]["weapon"]["name"],
            power=knightsconfig["lancelot"]["weapon"]["power"],
        ),
        armour=[
            Armour(part=a["part"], protection=a["protection"])
            for a in knightsconfig["lancelot"]["armour"]
        ],
        potion=Potion(
            name=knightsconfig["lancelot"]["potion"]["name"],
            effect=knightsconfig["lancelot"]["potion"]["effect"],
        )
        if knightsconfig["lancelot"]["potion"]
        else None,
    )

    arthur = Knight(
        name="Arthur",
        power=knightsconfig["arthur"]["power"],
        hp=knightsconfig["arthur"]["hp"],
        weapon=Weapon(
            name=knightsconfig["arthur"]["weapon"]["name"],
            power=knightsconfig["arthur"]["weapon"]["power"],
        ),
        armour=[
            Armour(part=a["part"], protection=a["protection"])
            for a in knightsconfig["arthur"]["armour"]
        ],
        potion=Potion(
            name=knightsconfig["arthur"]["potion"]["name"],
            effect=knightsconfig["arthur"]["potion"]["effect"],
        )
        if knightsconfig["arthur"]["potion"]
        else None,
    )

    mordred = Knight(
        name="Mordred",
        power=knightsconfig["mordred"]["power"],
        hp=knightsconfig["mordred"]["hp"],
        weapon=Weapon(
            name=knightsconfig["mordred"]["weapon"]["name"],
            power=knightsconfig["mordred"]["weapon"]["power"],
        ),
        armour=[
            Armour(part=a["part"], protection=a["protection"])
            for a in knightsconfig["mordred"]["armour"]
        ],
        potion=Potion(
            name=knightsconfig["mordred"]["potion"]["name"],
            effect=knightsconfig["mordred"]["potion"]["effect"],
        )
        if knightsconfig["mordred"]["potion"]
        else None,
    )

    red_knight = Knight(
        name="Red Knight",
        power=knightsconfig["red_knight"]["power"],
        hp=knightsconfig["red_knight"]["hp"],
        weapon=Weapon(
            name=knightsconfig["red_knight"]["weapon"]["name"],
            power=knightsconfig["red_knight"]["weapon"]["power"],
        ),
        armour=[
            Armour(part=a["part"], protection=a["protection"])
            for a in knightsconfig["red_knight"]["armour"]
        ],
        potion=Potion(
            name=knightsconfig["red_knight"]["potion"]["name"],
            effect=knightsconfig["red_knight"]["potion"]["effect"],
        )
        if knightsconfig["red_knight"]["potion"]
        else None,
    )

    lancelot.take_damage(mordred.total_power)
    mordred.take_damage(lancelot.total_power)
    arthur.take_damage(red_knight.total_power)
    red_knight.take_damage(arthur.total_power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
