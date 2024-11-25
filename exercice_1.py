def sum_of_digits(int) : 
  int_exp = str(int)

  sum = 0
  for i in range(len(int_exp)):
    digit = ord(int_exp[i]) - ord('0')
    sum += digit

  return sum