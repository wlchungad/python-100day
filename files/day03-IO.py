def main():
    while True:
        str_input = str(input("What is your name? ")).strip()
        if str_input:
            print(f"Hello {str_input}!")
            break
    
main()