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

    @narrative_speed(cps=3000)
    @staticmethod
    def event_start():
        print("In the Kingdom of Mateland, in the mid to late XI-th "
              "century, on a sunny spring day, a huge gatekeeper, a "
              "knight, asks for your name before allowing entry to "
              "the tournament")
        user_name = input("\n\nEnter your name: ")
        text = "\n\nLadies and gentlemen, welcome to the knight's " \
               "tournament!\nMy name is Roman the Apostle and I will " \
               "be hosting this thrilling tournament.\nToday is a " \
               "special day as we are honored to have with us the " \
               "KING himself -\nMATEthew the PYTHONheart, whose kindness " \
               "and support have helped us\nto organize this tournament" \
               " at the highest level!\nThank you all for joining us " \
               "today, and I hope you enjoy the show!"
        time.sleep(0.000001)

        return text

    @narrative_speed(cps=1000)
    @staticmethod
    def knights_fight(knight_1, knight_2):

        global event_counter
        if event_counter == 0:
            text = f"\n\n\nNoble guests and subjects, hear the proclamation!\n" \
                   f"In the battle of two knights, the one who strikes\n" \
                   f"the most crushing blow, shattering the opponent's\n" \
                   f"defense and bringing them to their knees, shall be\n" \
                   f"declared the victor of this contest!\n\nMoving on to" \
                   f"the list of participants who will fight for the\n" \
                   f"glory and honor of our kingdom!\nIn the first " \
                   f"match,{knight_1.name} and {knight_2.name} will " \
                   f"meet,\nready to demonstrate their warrior skills!\n\n" \
                   f"Armed to the teeth, {knight_1.name} prepares to\n" \
                   f"fight with a{knight_1.weapon['name']}, while\n" \
                   f"{knight_2.name} has chosen trusty\n" \
                   f"{knight_2.weapon['name']} to engage their\n" \
                   f"opponent. By the power of" \
                   f"{knight_1.name if knight_1.hp > knight_2.hp else knight_2.name}'s " \
                   f"mightieststrike, {knight_1.name if knight_1.hp < knight_2.hp else knight_2.name}" \
                   f"barely stand on his feet! The victory is declared " \
                   f"to belong to" \
                   f"{knight_1.name if knight_1.hp > knight_2.hp else knight_2.name}!"

            event_counter += 1
            return text

        else: #2
            text = f"\n\n Attention, noble guests and subjects! " \
                   f"The first battle of our " \
                   f"tournament was so fiery that even the dragon on " \
                   f"our coat of arms wondered if it should join the " \
                   f"fray. However, we have yet another clash before " \
                   f"us, in which two unwavering knights will face " \
                   f"off.{knight_1.name} and {knight_2.name}, raise " \
                   f"your weapons and fight on the honorable " \
                   f"battlefield, without shields but with all the " \
                   f"chivalrous manners!In this battle, the winner " \
                   f"will be the one who demonstrates the highest " \
                   f"agility and mastery of their weapon."
            return text

# In the next pair, we will see Knight_3 with a spear and Knight_4 with a sword and round shield, whose battle hymn is already sounding around us! Get ready for exciting battles!
# Let the fight begin!
