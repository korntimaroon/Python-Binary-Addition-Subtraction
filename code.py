import time
import random
import os

def decimalToBinary(n):
  return bin(n).replace("0b", "")

def binaryToDecimal(n): 
  return int(n, 2) 


  
while True:
  binaryNum = []
  for i in range(0,2):
    if i == 1:
      binaryNum.append(random.randint(0,binaryNum[0]))
    else: 
      binaryNum.append(random.randint(0,255))
  try:
    choices = int(input("Addition (1) or Subtraction (2): "))
  except:
    break
  if choices == 1:
    ans=input(decimalToBinary(binaryNum[0]) + " + " + decimalToBinary(binaryNum[1]) + " = ")
    try:
      print("Answer: ", decimalToBinary(int(binaryNum[0] + binaryNum[1])), ", ", (int(binaryNum[0] + binaryNum[1])), ", //// ", binaryToDecimal(ans) == int(binaryNum[0] + binaryNum[1]), " \\\\\\\ , enter to next question")
      input()
    except:
      print("Not Binary format, Enter to the next question")
      input()
      os.system('clear')
      continue
    os.system('clear')
  elif choices == 2:
    ans=input(decimalToBinary(binaryNum[0]) + " - " + decimalToBinary(binaryNum[1]) + " = ")
    try:
      print("Answer: ", decimalToBinary(int(binaryNum[0]) - int(binaryNum[1])), ", ", int(binaryNum[0] - binaryNum[1]), ", //// ", binaryToDecimal(ans) == int(binaryNum[0] - binaryNum[1]), "\\\\\\\\, enter to the next question")
      input()
      os.system('clear')
    except:
      print("Not Binary format, Enter to the next question")
      input()
      os.system('clear')
      continue
  else:
    print("Between 1 and 2")
    time.sleep(0.7)
    os.system('clear')
    continue
