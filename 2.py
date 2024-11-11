def input_validation(number):
    if not number.isdigit() and not number.startswith('0b'):
        print("Invalid input, try again")
        return False
    return True

def two_ten(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number

def ten_two(decimal_number):
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number

while True:
    number = input("Write the number which you want to convert: ")
    if not input_validation(number):
        continue
    if number.startswith('0b'):
        decimal_number = two_ten(number)
        print(f"Decimal: {decimal_number}")
    else:
        decimal_number = int(number)
        binary_number = ten_two(decimal_number)
        print(f"Binary: {binary_number}")

    choice = input("Do you want to convert more numbers (yes/no): ").lower()
    if choice == "no":
        break
