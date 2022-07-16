def calculate_exponent(base_number, exponent_number):
    return int(base_number)**int(exponent_number)

print("The result is " + str(calculate_exponent(base_number=input("Please enter the base number.\n"), exponent_number=input("Please enter the exponent number.\n"))))