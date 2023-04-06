import os
import time


os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


event_counter = 0


class Event:

    def narrative_speed(cps):
        def decorator(func):
            def wrapper(*args, **kwargs):
                text = str(func(*args, **kwargs))
                for char in text:

                    print(char, end='', flush=True)
                    time.sleep(1 / cps)
            return wrapper
        return decorator

    @staticmethod
    def ambience():
        pygame.init()
        pygame.mixer.music.load('CR_TourneyBattle01UniWalk.mp3')
        pygame.mixer.music.play()

    @narrative_speed(cps=1000)
    @staticmethod
    def event_start():
        print("In the Kingdom of Mateland, in the mid to late XI-th century")
        text = ("\n\nLadies and gentlemen, welcome to the knight's tournament!\n"
                "My name is Roman the Apostle and I will be hosting this\n"
                "thrilling tournament.\nToday is a special day as we are honored to\n"
                "have with us the KING himself - MATEthew the PYTHONheart, whose\n"
                "kindness and support have helped us to organize this tournament\n"
                "at the highest level!\nThank you all for joining us today, and I "
                "hope you enjoy the show!")
        return text
    @narrative_speed(cps=1000)
    @staticmethod
    def event_fight(knight_1, knight_2):

        global event_counter
        if event_counter == 0:
            text = (f"\n\n\nNoble guests and subjects, hear the proclamation!\n"
                    f"In the battle of two knights, the one who strikes the most crushing\n"
                    f"blow, shattering the opponent's defense and bringing them to their\n"
                    f"knees, shall be declared the victor of this contest!\n\nMoving on to"
                    f"the list of participants who will fight for\nthe glory and honor of our "
                    f"kingdom!\nIn the first match,{knight_1.name} and {knight_2.name}\n"
                    f"will meet, ready to demonstrate their warrior skills!\n\nArmed to"
                    f"the teeth, {knight_1.name} prepares to fight with a\n"
                    f"{knight_1.weapon['name']}, while {knight_2.name} has chosen trusty\n"
                    f"{knight_2.weapon['name']} to engage their opponent.\n\nBy the power "
                    f"of {knight_1.name if knight_1.hp > knight_2.hp else knight_2.name}'s "
                    f"mightiest strike,"
                    f"{knight_1.name if knight_1.hp < knight_2.hp else knight_2.name}"
                    f" barely stand on his feet!\nThe victory is declared to "
                    f"belong to {knight_1.name if knight_1.hp > knight_2.hp else knight_2.name}!")

            event_counter += 1
            return text

        else: #2
            text = f"\n\nAttention, noble guests and subjects!\n" \
                   f"The first battle of our tournament was so fiery that even the " \
                   f"dragon on our coat of arms wondered if it should join the fray!\n" \
                   f"However, we have yet another clash before us, in which two " \
                   f"unwavering\nknights will face off.\n{knight_1.name} and {knight_2.name}, " \
                   f"raise your weapons and fight on the honorable battlefield, " \
                   f"without shields but with all the chivalrous manners!\n" \
                   f"In this battle, the winner will be the one who demonstrates the " \
                   f"highest agility and mastery of their weapon.\n\n{knight_1.name} fights " \
                   f"with his {knight_1.weapon['name']}, demonstrating his elegance and " \
                   f"precision, while the {knight_2.name} wields a {knight_2.weapon['name']}, " \
                   f"showcasing his strength and power.\nBoth knights hold their ground " \
                   f"very closely, trying to find a vulnerable spot in their opponent's " \
                   f"defense.\nFinally, {knight_1.name if knight_1.hp > knight_2.hp else knight_2.name} " \
                   f"makes a swift strike that evades the {knight_1.name if knight_1.hp < knight_2.hp else knight_2.name}'s " \
                   f"defense and chops down to his thigh.\nThe " \
                   f"{knight_2.name if knight_2.hp < knight_1.hp else knight_1.name} falls " \
                   f"to his knees, admitting defeat.\n\nCongratulations to " \
                   f"{knight_1.name if knight_1.hp > knight_2.hp else knight_2.name} " \
                   f"on his victory in this thrilling battle!"

            return text

    @narrative_speed(cps=1000)
    @staticmethod
    def event_result(result):

        items = result.items()
        result = [[k, v] for k, v in items]
        result.sort(key=lambda x: x[1], reverse=True)

        text = (
            "Based on the results of two battles, our judges have awarded the following number of "
            f"points to our participants:\n\n{'*' * 10}\n"
            f"{result[0][0]}: {result[0][1]}\n"
            f"{result[1][0]}: {result[1][1]}\n"
            f"{result[2][0]}: {result[2][1]}\n"
            f"{result[3][0]}: {result[3][1]}\n{'*' * 10}\n\n"
            f"Ladies and gentlemen, it is my honor to declare the winner of the tournament, Sir {result[0][0]}! "
            f"As the champion, Sir {result[0][0]} has the privilege of challenging anyone in the audience "
            "to a duel. Who among you dares to face this valiant knight?")

        return text


