import time


def event_start():
    text = "Ladies and gentlemen, welcome to the grandest knight tournament in the entire " \
           "kingdom!" \
           "\nHere, the most powerful and brave knights will come together to " \
           "determine who will become the true hero.\nDear guests, if you believe that you " \
           "have the spirit of a true knight, you can join our fighters!\nChoose your " \
           "equipment and head to the arena!\n__________________________________________" \
           "___________________________________________\n" \
           "\"Take part!\" ->                                                    enter " \
           "\"yes\"\n\"Refuse and " \
           "choose a place with a better view\" " \
           "->                  enter \"no\" \n"
    cps = 10000
    for char in text:
        print(char, end='', flush=True)
        time.sleep(1 / cps)

    # scenario = input("\nWhat will you choose?:                                                   ")
