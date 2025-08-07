
ALPHABET = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
def encrypt(unencrypted_text, shift_num:int):
    # create a moved alphabet list
    encrypted_dict = []
    for character in unencrypted_text:
        encrypted_dict.append(ALPHABET[ALPHABET.find(character)+shift_num])
    return ''.join(encrypted_dict) 

def decrypt(encrypted_text, passkey:int): 
    decrypted_text = []
    for character in encrypted_text:
        decrypted_text.append(ALPHABET[ALPHABET.find(character)-passkey])
    return ''.join(decrypted_text)

def main():
    while True: 
        text = str(input("Text: ")).strip().lower()
        key = int(input("Key: "))
        action = str(input("[E]ncrypt / [D]ecrypt / [EXIT]: "))
        if action in ['e', 'E', '[E]ncrypt', 'Encrypt']:
            ans = encrypt(text, key)
        elif action in ['d', 'D', '[D]ecrypt', 'decrypt']:
            ans = decrypt(text, key)
        print ("Result: %s" % ans)
    return

main()