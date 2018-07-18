num1 = input ('string 1: ')
num2 = input('string 2: ')

set_1 = set((num.strip()) for num in num1.split(', '))
set_2 = set((num.strip()) for num in num2.split(', '))

result = [int(num) for num in set_1.intersection(set_2)]
result.sort()
result = ', ' .join(str(x) for x  in result)
print(result)
