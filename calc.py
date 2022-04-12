x=0
while x==0:
    resulttxt =open("results.txt" ,"a")

    #dictionary
    op_convert = {
        "+" : "add",
        "-" : "sub",
        "/" : "div",
        "*" : "multi",
        "^" : "sqr"
    }

    #Input Variables
    firstNum = int(input("Enter First Number:"))
    operator = input("Enter The Operator:")
    secondNum = int(input("Enter Second Number:"))
    global result 

    #Functions
    def add():
        global result 
        result= firstNum + secondNum
        print(result)
    def sub():
        global result 
        result = firstNum - secondNum
        print(result)
    def multi():
        global result 
        result = firstNum * secondNum
        print(result)
    def div():
        global result 
        result = firstNum / secondNum
        print(result)
    def sqr():
        global result 
        result = firstNum**secondNum
        print(result)

        
    #If Entered A Opertor
    if operator == "+" or "-" or "/" or "*":
        op = op_convert[operator]
        eval(op+"()")
    else:
        print("Invalid Values")

    #Write Results To A File
    resulttxt =open("results.txt" ,"a+")
    str(result)
    resulttxt.write("\n" + str(result))
    resulttxt.close()
