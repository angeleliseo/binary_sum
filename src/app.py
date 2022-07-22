
"""
Given 2 strings that contains a binary number (only 0 or 1)
Create a program that add 2 binary numbers and print the result. 
  
"""

#Global variables to control the current carry and the future carry to be used
#on next column / for iteration.
currentCarry = 0
nextCarry = 0

def main(bin1, bin2):

  #Input data
  #bin1 = "111110111"
  #bin2 = "111001"

  #variable to store the final result
  result = ""

  #required to use the variables as global
  global currentCarry
  global nextCarry

  #Addressing the different len input strings
  bin1, bin2 = match_len(bin1,bin2)

  arr_len = len(bin1)

  for element in range(arr_len-1,-1,-1):
    nextCarry = 0
    res = sum_binary(currentCarry, int(bin1[element]))
    result = result + str(sum_binary(res, int(bin2[element])))
    currentCarry = nextCarry
  
  if nextCarry == 1:
    result = result + str(nextCarry)
  print("The result is: %s " % result[::-1])
  return result[::-1]

def sum_binary(num1, num2):
  """
  Acept 2 numbers 0 or 1 and apply the addition binary logic.
  
  Args:
      num1 (int): first 0 or 1 integer that represent the binary digit to add
      num2 (int): second 0 or 1 integer that represent the binary digit to add

  Returns:
      int: result of the add operation in binary numberical system. When
      adding 1 + 1 it returns 0 and considr a carry.
  """
  #global variable to control the carry to be used in the next column addition.
  global nextCarry
  if num1 == 1 and num2 == 1:
    nextCarry = nextCarry + 1
    return 0
  elif num2 != num1:
    nextCarry = nextCarry + 0
    return 1
  else:
    nextCarry = nextCarry + 0
    return 0

def match_len(str1, str2):
  """
  Given 2 strings as output consider the len of the bigger as reference len.
  and force match the len of the smaller string filling with '0' characters
  at the left.
  Sample:
    if string 'aaaa' is given as str1 and 'bb' is given as str2 then it will
    return 2 strings like this: 'aaaa' and '00bb'

  Args:
      str1 (str): First string to conssier on the len matching
      str2 (str): Secon string to conssider on the len matching
  Returns: 
    str str
  """

  res = ""
  if len(str1) > len(str2):
    to_fill = len(str1) - len(str2)
    for var_char in range(to_fill):
      res = res + "0"
    return str1, (res + str2)
  elif len(str1) < len(str2):
    to_fill = len(str2) - len(str1)
    for var_char in range(to_fill):
      res = res + "0"
    return (res + str1), str2
  else:
    return str1, str2
