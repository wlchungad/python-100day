todo_list = []

def add_item():
    item = str(input("What is the next task? "))
    todo_list.append(item)

def change_item():
    print_todo_list()
    replace_no = int(input("What is the task to be renewed? "))
    new_item = str(input("What is the new task? "))
    todo_list[replace_no-1] = new_item

def delete_item():
    index_no = int(input("Please enter the item number to be removed: "))
    if (str(input("Are you sure? (Y/N)"))) == 'Y' & index_no <= (len(todo_list)-1):
        print(f"Item \"{todo_list.pop(index_no)}\" is removed.")

def print_todo_list():
    if todo_list:
        print("Items:")
        for i, item in enumerate(todo_list):
            print(f"Item {i+1} - {item}")
    else:
        print("No work item for now. Add one now!")

def main():
    print ("Welcome back to the to-do list!")
    while True:
        print('---' * 10)
        user_option = str(input("What do you need? (view/add/replace/delete) ")).strip().lower()
        match user_option:
            case "view": print_todo_list()
            case "add": add_item()
            case "replace": change_item()
            case "delete": delete_item()
            case _: continue

main()