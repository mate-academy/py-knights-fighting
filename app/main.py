from app.knights.lancelot import lancelot as lanc
from app.knights.arthur import arthur as art
from app.knights.mordred import mordred as mor
from app.knights.red_knight import red_knight as rk


def battle(dictionary: dict) -> dict:

    result_lancelot = lanc(dictionary)
    result_mordred = mor(dictionary)
    result_arthur = art(dictionary)
    result_red_knight = rk(dictionary)

    lancelot = dictionary["lancelot"]
    mordred = dictionary["mordred"]
    arthur = dictionary["arthur"]
    red_knight = dictionary["red_knight"]

    lancelot["name"] = result_lancelot[0]
    lancelot["hp"] = result_lancelot[1]
    lancelot["protection"] = result_lancelot[2]
    lancelot["power"] = result_lancelot[3]
    mordred["name"] = result_mordred[0]
    mordred["hp"] = result_mordred[1]
    mordred["protection"] = result_mordred[2]
    mordred["power"] = result_mordred[3]
    arthur["name"] = result_arthur[0]
    arthur["hp"] = result_arthur[1]
    arthur["protection"] = result_arthur[2]
    arthur["power"] = result_arthur[3]
    red_knight["name"] = result_red_knight[0]
    red_knight["hp"] = result_red_knight[1]
    red_knight["protection"] = result_red_knight[2]
    red_knight["power"] = result_red_knight[3]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
