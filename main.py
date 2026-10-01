from pyscript import document

def compute(event):

    num1 = float(document.querySelector("#num1").value)
    num2 = float(document.querySelector("#num2").value)

    operation = document.querySelector("#operation").value

    if operation == "+":
        answer = num1+num2

    if operation == "-":
        answer = num1-num2

    if operation == "*":
       answer = num1*num2

    if operation == "/":

     if num2 == 0:
       document.querySelector("#result").innerText = "Cant divide by zero bro" 
       return

       answer = num1/num2