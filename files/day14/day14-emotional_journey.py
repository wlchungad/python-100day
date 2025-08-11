import json
from pprint import pprint
from pathlib import Path
from datetime import date

JOURNAL_FILE = Path('journey.txt')
# print(JOURNAL_FILE)

CMD_EXIT = ['e', 'exit']
CMD_READ = ['r', 'read']
CMD_WRITE = ['w', 'write']
CMD_DELETE = ['d', 'delete']
VALID_CMD = CMD_EXIT + CMD_READ + CMD_WRITE + CMD_DELETE
#   grinning squinting face -> U+1F606 -> U0001F606
#   knocked-out face -> U+1F635 -> U0001F635
EMOJI_LIST = ["\U0001F635", "\N{unamused face}", "\N{face without mouth}", "\N{winking face}", "\U0001F606"]

dict_emotions = {}

def read_emotions():
    # read file
    with open(JOURNAL_FILE, "r") as file:
        lines = file.readlines()
    # convert the line of JSON to dictionary
    # format: 
    # {
    #   "YYYY/MM/DD": {"Score": (1-5), "incident": text message},
    #   "YYYY/MM/DD": {"Score": (1-5), "incident": text message}, 
    #   {...}
    # }
    for line in lines:
        single_item = json.loads((line))
        # print(single_item.keys())
        dict_emotions.update(single_item)

def show_emotions():
    if dict_emotions:
        print("The emotion scales from 1 to 5")
        print("Scale:\t  1\t --\t--\t--\t  5")
        print(f"Emoji:\t {EMOJI_LIST[0]}\t --\t{EMOJI_LIST[2]} \t--\t {EMOJI_LIST[4]}")
        # pprint(dict_emotions)
        # # print(len())
        # print(json.dumps(
        #     dict_emotions,
        #     sort_keys=True,
        #     indent=2,
        #     separators=(',', ': ')
        # ))
        for i ,record_key in enumerate(dict_emotions):
            emotion_record = dict_emotions[record_key]
            print(f"Item {i+1}:")
            print(f"Date: {emotion_record["Date"]}")
            print(f"Incident: {emotion_record["incident"]}")
            print(f"Feeling: {emotion_record["Score"]} ({EMOJI_LIST[emotion_record["Score"]-1]})")
            
    else:
        print("No record yet")

def write_emotions():
    last_key = list(dict_emotions.keys())[-1]
    while True:
        score_input = (input("How are you today? (at least 1, 5 at most)").strip().lower())
        try:
            score_input = int(score_input)
        except: 
            continue
        if (1 <= score_input <= 5):
            break
    while True:
        Incident_input = input("What happened?").strip()
        if Incident_input: break
    single_record = {
        str(int(last_key)+1): {
            "Date": str(date.today()),
            "Score": score_input, 
            "incident": Incident_input
            }
        }
    dict_emotions.update(single_record)
    print("Emotion recorded.")

def remove_emotions():
    # print("Please do not neglect your feeling")
    return

def close_file():
    with open(JOURNAL_FILE, "w") as file:
        file.write(json.dumps(dict_emotions))

def interface():
    exited = False
    try:
        print('-'*10, 'Start', '-'*10)
        while not exited:
            while True:
                option_input = input("How can I help? ").strip()
                if (option_input in VALID_CMD) :
                    break
                elif not option_input:
                    continue
                else:
                    print ("invalid command")
            match option_input:
                case option_input if option_input in CMD_READ: show_emotions()
                case option_input if option_input in CMD_WRITE: write_emotions()
                case option_input if option_input in CMD_DELETE: remove_emotions()
                case option_input if option_input in CMD_EXIT: exited = True
                case _: break
    except KeyboardInterrupt:
        return 0

def main():
    read_emotions()
    interface()
    close_file()
    print("\nGoodbye, have a nice day")
    print('-'*10, 'End', '-'*10)
    return 0

if __name__ == "__main__":
    main()