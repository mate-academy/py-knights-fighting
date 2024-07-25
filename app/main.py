from app.god.god import God
from app.prototype import *
from app.human.knight import Knight


def battle(knightsConfig):
    l_squire = God.arise_servant("Lancelot's_squire")
    a_squire = God.arise_servant("arthur's_squire")
    m_squire = God.arise_servant("mordred's_squire")
    r_squire = God.arise_servant("red_knight's_squire")

    lancelot = Knight("Lancelot", 35, 35, )


battle(KNIGHTS)
