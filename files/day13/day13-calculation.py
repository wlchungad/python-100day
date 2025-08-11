import re
INVALID_CHARS = r'\\!@#$%^&\(\)\[\]\{\}'

def main():
    while True:
        formula = str(input("Formula: ")).strip()
        if any(char.isalpha() for char in formula) or (re.match(INVALID_CHARS, formula)):
            print("Invalid formula: alphabet detected")
            continue
        if not formula:
            continue
        break
    try:
        numbers = re.split(r'\+|\-|\*|\/',formula)
        #print(numbers)
    except:
        print ("Cannot split the formula %s" % formula)
        return -1

    try:
        formula_copy = formula
        for num in numbers:
            formula_copy = formula_copy.replace(num, "")
        operators = [char for char in formula_copy]
        #print(operators)
    except:
        print ("Cannot get the operators: %s" % formula)
        return -1

    try:
        # try:
        #     res = float(numbers[0])
        # except:
        #     res = 0
        # for i, op in enumerate(operators):
        #     match op:
        #         case '+': res += float(numbers[i+1])
        #         case '-': res -= float(numbers[i+1])
        #         case '*': res *= float(numbers[i+1])
        #         case '/': res /= float(numbers[i+1])
        res = eval(formula)
        if res.is_integer():
            res = int(res)
        print (f"Result: {res}")
    except ZeroDivisionError:
        print ("Invalid formula '%s': Zero division detected!" % formula)
        return -1
    except IndexError as idxerr:
        print (f"IndexError: {idxerr}")
        return -1
    return 0

if __name__ == "__main__":
    main()