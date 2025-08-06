import time
import random
import re

pharses = ["FLOWER", "LEAFY", "FIREY", "SPONGY"]

graphes = [
    """
    -----
    |   |
    |
    | 
    | 
    |
    ---------
    """,
    """
    -----
    |   |
    |   o
    | 
    | 
    |
    ---------
    """,
    """
    -----
    |   |
    |   o
    |   |
    | 
    |
    ---------
    """,
    """
    -----
    |   |
    |   o
    |  /|
    | 
    |
    ---------
    """,
    """
    -----
    |   |
    |   o
    |  /|\\
    | 
    |
    ---------
    """,
    """
    -----
    |   |
    |   o
    |  /|\\
    |  /
    |
    ---------
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |  / \\
    |
    ---------
    """]
# for graph in graphes:
#     print(graph)
#     time.sleep(1)
def main():
    # init
    live_point = len(graphes)
    keyword = random.choice(pharses)
    # print ("The keyword is ... %s" % keyword)
    user_answer = ["_"]  * len(keyword)
    print('---Game start---')
    print("...You have %d lives" % live_point)
    print("Hint: the keyword has %d letters" % len(keyword))
    while live_point > 0:
        print(graphes[len(graphes)-live_point])
        print("Progress: %s" % user_answer)
        
        while True:
            user_input = str(input("Please choose a letter: ")).upper()
            if user_input.isalpha() and len(user_input) == 1:
                break
            print("WARN: Invalid input! ")
        
        if user_input in keyword:
            print ("You found a correct letter!")
            # find the index
            char_indexes = [m.start() for m in re.finditer(user_input, keyword)]
            # update temp key
            for char_index in char_indexes:
                user_answer[char_index] = user_input

        else:
            print ("That is not correct")
            live_point -= 1

        if ''.join(user_answer) == keyword or live_point == 0: 
            break
    print('----------')
    if live_point > 0:
        print("Game clear! Congulations!")
        print("With %d lives left, you succesfully guessed the word!" % live_point)
        print("The keyword of the day is \"%s\"!" % keyword)
    else: 
        print("Game over...")
    return

main()