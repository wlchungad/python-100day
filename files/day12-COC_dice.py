import random

def random_integer(start=0, end=9):
    return random.randint(start,end)

def test_case():
    print('-' * 10, "START", '-'*10)
    print("Note: this is just a test case.")
    print("Player rolling...")
    effect = random_integer(-10, 10)
    print(f"The buff is {effect}")
    player_stat = random_integer()*10 + random_integer() + effect
    print("Encounter rolling...")
    KP_stat = random_integer()*10 + random_integer() - effect
    difference = player_stat-KP_stat
    print(f"Stat difference: {player_stat} / {KP_stat} = {(difference)}")
    if difference < 0:
        print("Player cannot succeed.")
        print("Simulation ended.")
        return
    elif difference <= 5:
        print("That would be difficult...")
    elif difference > player_stat or KP_stat <= 0:
        print("Defaulting to success!")
        print("Simulation ended.")
        return
    
    pl_roll = random_integer()*10 + random_integer() + effect
    print(f"The player rolled {pl_roll}/{difference}")
    if (pl_roll < difference):
        if pl_roll <= 5:
            print("Huge success!")
        elif (pl_roll - difference) < 5: 
            print("That was a close call, but Success!")
        else: 
            print("Success!")
    elif (pl_roll == difference):
        print("That is a special case. Please ask KP for decision.")
    else:
        if pl_roll >= 95:
            print("Epic fail!")
        elif (pl_roll - difference) < 5: 
            print("That was a close one.")
        else: 
            print("Failed.")

    print("Simulation ended.")
    return

def main():
    test_case()

main()