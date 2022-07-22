from src.app import main

def test_canary():
  assert True, "Environment has issues"

def test_binary_sum_static():
  # we know the result of the given sum is 1000110000
  # used arguments 111110111 and 111001
  assert main("111110111", "111001") == "1000110000"

def test_compare_with_lib():
  # Given known cases 111110111 and 111001
  # using another different convertion way to sum in binary
  bin1 = "0b111110111"
  bin2 = "0b111001"

  #converting binary input into integer and then summing
  int_sum = int(bin1, 2) + int(bin2, 2)

  #re converting the interger result into binary again
  bin_sum = bin(int_sum)

  ret = main("111110111", "111001")
  #adding 0b to the string to be in same binary string format to match
  #bin function output
  assert "0b{}".format(ret) == bin_sum

  