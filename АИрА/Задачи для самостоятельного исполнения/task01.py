number = 23007

result = "+".join(str(int(digit) * 10**(len(str(number))-index-1)) for index, digit in enumerate(str(number)))
print(result)