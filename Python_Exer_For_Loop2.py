usr_input = int(input('Please enter a number: '))
for x in range(2,usr_input+1):
    if usr_input%x == 0 and usr_input!=x :
        print('The number you inputted is not a prime number.')
        break
else: 
    print('The number you inputted is a prime number.')    