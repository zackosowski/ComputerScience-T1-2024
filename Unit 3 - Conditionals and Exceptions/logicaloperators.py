# Logical Operators
# Arithmetic Operators + - * / // ** %
# Comparison Operators > < >= <= ==
# Logical Operators and or !
# AND means that BOTH conditions must be true
# OR means that at least one condition must be true
# ! (not) means the inverse, ex. != (not equal to)

def check_eligibility(age, exp):
    if age >= 18 and exp >=1:
        print("You are eligible!")

    else:
        print("You are not eligible...")

check_eligibility()
