in_numbers = input("input the numbers seperated by a -: ")
list_1 = [int(x.strip()) for x in in_numbers.split('-')]
result = {num: num**2 for num in list_1}
print(result)
