#Dictionary
op_convert = {
    "+" : "add",
    "-" : "sub",
    "/" : "div",
    "*" : "multi",
}

#Input Variables
firstNum = int(input("Enter First Number:"))
operator = input("Enter The Operator:")
secondNum = int(input("Enter Second Number:"))

#Functions
def add():
    result = firstNum + secondNum
    print(result)
def sub():
    result = firstNum - secondNum
    print(result)
def multi():
    result = firstNum * secondNum
    print(result)
def div():
    result = firstNum / secondNum
    print(result)

#If Entered A Opertor
if operator == "+" or "-" or "/" or "*":
    op = op_convert[operator]
    eval(op+"()")

