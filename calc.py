firstNum = input("Enter First Number :- ")
secondNum = input("Enter Second Number :- ")
exp = input("Enter The Expression(+,-,*,/):  ")

if exp == "+":
    value = int(firstNum) + int(secondNum)
    print("Answer Is: " + str(value))
elif exp == "-":
    value = int(firstNum) - int(secondNum)
    print("Answer Is: " + str(value))
elif exp == "*":
    value = int(firstNum) * int(secondNum)
    print("Answer Is: " + str(value))
elif exp == "/":
    value = int(firstNum) / int(secondNum)
    print("Answer Is: " + str(value))