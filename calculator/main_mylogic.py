from art import logo
import os
clear = lambda : os.system('cls')
print(logo)

def sum(n1,n2):
  """Returns sum of given 2 values (arguments)"""
  sum_res = n1 + n2
  return sum_res

def sub(n1,n2):
  """Returns Substraction of given 2 values (arguments)"""
  sub_res = n1 - n2
  return sub_res

def mul(n1,n2):
  """Returns Multiplication of given 2 values (arguments)"""
  mul_res = n1 * n2
  return mul_res

def div(n1,n2):
  """Returns Division of given 2 values (arguments)"""
  div_res = n1 / n2
  return div_res


operations = ['+','-','*','/']
new_calc = True

while new_calc == True:
  total = 0
  firstNum = float(input("Enter a number : "))
  continue_calc = True
  while continue_calc == True:
    print("""+
-
*
/""")
    op = input("pick an operation : ")
    
    if op in operations:
      secNum = float(input("Enter 2nd number: "))
      if op == "+":
        total= sum(firstNum,secNum)
        print(f"{firstNum} + {secNum} = {total}")
      if op == "-":
        total= sub(firstNum,secNum)
        print(f"{firstNum} - {secNum} = {total}")
      if op == "*":
        total= mul(firstNum,secNum)
        print(f"{firstNum} * {secNum} = {total}")
      if op == "/":
        total= div(firstNum,secNum)
        print(f"{firstNum} / {secNum} = {total}")
    else:
      print("Dont be oversmart.")
      # continue_calc = False
    new_cal = input(f"Type 'y' to continue with {total}, or type 'n' to start a new calc: ").lower()
    if new_cal == 'y':
      firstNum = total
    elif new_cal == 'n':
      continue_calc=False
      clear()
    else:
      print("I am just a calculator. Input proper y or n . ")
      new_calc = False
      continue_calc = False