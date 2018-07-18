in_number = input("input the numbers: ")
list_1 = [int(x) for ind,x in enumerate(in_number.split(',')) if ind%2!=0]
list_2 = [int(y) for ind,y in enumerate(in_number.split(',')) if ind%2==0]

zipped = list(zip(list_2,list_1))

print(zipped)

