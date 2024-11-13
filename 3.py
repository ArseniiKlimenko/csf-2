def input_validation(number):
    if 'x' in number:
        valid = number.split('x')
        if not valid[0].isalnum or not valid[1].isdigit():
            print("Invalid input, try again")
            return False
        base = int(valid[1])
        if base < 2 or base > 16:
            print("Invalid base, try again")
            return False
        another = int(valid[0])
        if base == 2 and another > 1:
            print("Invalid base, try again")
            return False
    elif not number.isdigit():
        print("Invalid input, try again")
        return False
    return True

def any_to_decimal(num, base):
    return int(num, base)

def decimal_to_any(decimal_number, base):
    digits = "0123456789ABCDEF"
    result = ""
    while decimal_number > 0:
        result = digits[decimal_number % base] + result
        decimal_number = decimal_number // base
    return result

while True:
    number = input("Write the number which you want to convert(123x4 or 123): ")
    if not input_validation(number):
        continue

    if 'x' in number:
        num, base = number.split('x')
        base = int(base)
        decimal_number = any_to_decimal(num, base)
    else:
        decimal_number = int(number)

    new_base = int(input("Enter to which system you want to convert the number (2-16): "))
    if new_base < 2 or new_base > 16:
        print("Invalid base, try again")
        continue
    converted_number = decimal_to_any(decimal_number, new_base)
    print(f"{number} = {converted_number}x{new_base}")

    choice = input("Do you want to convert more numbers (yes/no): ").lower()
    if choice == "no":
        break
