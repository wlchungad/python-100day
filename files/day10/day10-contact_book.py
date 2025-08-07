ALLOWED_ACTIONS = ['v', 'view',
                   'q', 'query',
                   'a', 'append', 
                   'u', 'update', 
                   'e', 'exit']
contact_book = {}

def get_personal_info():
    import re
    while True:
        name_input = str(input("Name: ")).strip().lower()
        if name_input:
            break
    while True:
        phone_input = str(input("Phone number: ")).strip()
        phone_input.replace(' ', '')
        if re.match(r'^\+\d{8,13}$', phone_input) or re.match(r'^\d{8,13}$', phone_input):
            break
    while True:
        mail_input = str(input("E-mail: ")).strip().lower()
        if re.match(r'^[a-z]+\@[a-z]+\.[a-z]+$', mail_input):
            break
    return name_input, phone_input, mail_input

def view_contact_book():
    if contact_book != {}:
        for x, y in contact_book.items():
            print(f"Name: {x}\nPhone: {y['Phone']}\nMail: {y['Mail']}")
    else: 
        print("No item")

def query_contact_book(name=None):
    if not name:
        while True:
            name_query = str(input("Name: ")).strip().lower()
            if name_query:
                break
        name = name_query
    print("Checking for records...")
    if name in contact_book.keys():
        print(contact_book.get(name))
        return True
    return False

def append_contact_book(name_append=None, phone_append=None, mail_append=None):
    print("Adding new records...")
    if not name_append or not phone_append or not mail_append:
        name_append, phone_append, mail_append = get_personal_info()
    
    if query_contact_book(name_append):
        update_contact_book(name_append, phone_append, mail_append, 'append')
    
    contact_book.update({name_append:
                         {"Phone":phone_append,
                           "Mail":mail_append}})
    print("Added new records.")
    
def update_contact_book(name=None, phone=None, mail=None, source=['append', 'prompt']):
    
    if source == 'append':
        print("Try to overwrite...")
        if (str(input("Please confirm (Y/N):")).upper()) == "Y":
            if not name: return
            if phone:
                contact_book[name]["Phone"] = phone
            if mail:
                contact_book[name]["Mail"] = mail

    elif source == 'prompt':
        print("Updating new records...")
        name_update, phone_update, mail_update = get_personal_info()
        if query_contact_book(name_update):
            if phone:
                contact_book[name_update]["Phone"] = phone_update
            if mail:
                contact_book[name_update]["Mail"] = mail_update
        else: 
            append_contact_book(name_update, phone_update, mail_update)
        
    return

def main():
    exited = False
    while not exited:

        while True:
            operation_input = str(input("Command: ")).strip().lower()
            if operation_input.isalpha() and (operation_input in ALLOWED_ACTIONS):
                break
        
        match operation_input:
            case 'v' | 'view': view_contact_book()
            case 'q' | 'query': query_contact_book()
            case 'a' | 'append': append_contact_book()
            case 'u' | 'update': update_contact_book(source='prompt')
            case 'e' | 'exit': exited = True

        continue    

if __name__ == "__main__":
    main()