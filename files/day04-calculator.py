def main():
    while True:
        float_input_1 = float(str(input("First number: ")).strip())
        if not float_input_1:
            #print(f"Hello {str_input}!")
            continue
        operation = str(input("Operation (+ - * /): "))
        if not operation in ['+', '-', '*', '/']: 
            continue
        float_input_2 = float(str(input("Second number: ")).strip())
        if not float_input_2:
            #print(f"Hello {str_input}!")
            continue
        match operation:
            case '+' : print(f"{float_input_1} {operation} {float_input_2} = {float_input_1+float_input_2}")
            case '-' : print(f"{float_input_1} {operation} {float_input_2} = {float_input_1-float_input_2}")
            case '*' : print(f"{float_input_1} {operation} {float_input_2} = {float_input_1*float_input_2}")
            case '/' : print(f"{float_input_1} {operation} {float_input_2} = {float_input_1/float_input_2}")
            case _: break 

main()