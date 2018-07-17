#1
# =============================================================================
usr_input = int(input("Enter a number: "))
list = []

result = [num for num in range(1,usr_input+1) if num%2 ==0]
print(result)
   
# =============================================================================

#2
# =============================================================================
usr_input = int(input("Enter a number: "))
divisible_by = int(input("Enter a number divisible by : "))
list = []
 
for x in range (1,usr_input + 1):
    if x%divisible_by ==0:
        list.append(x)
list.sort()        
print(list)     
# =============================================================================

#3
list1 = [0, 3, 6, 9, 10, 2, 5]
list2 = [2, 6, 4, 7, 8, 1, 15]

result = [str for str in list1 if str in list2]   
print(result)

#4
usr_input = int(input("Enter a number: "))
till_number = int(input("Till which number : "))

result = [usr_input*num for num in range (1,usr_input+1) if usr_input * num < till_number]
print(result)


#    

