import random
def throw_dice(l1):
    dice_list = l1 
    new_list = []
    
    for i in range(3):
        x = random.randint(1,len(dice_list)-1)
        print ("Removing {} from the list".format(dice_list[x]))
        dice_list.pop(x)  
       
    for i in range(2):
        x = random.randint(1,len(dice_list)-1) 
        print ("Picking {} from the list".format(dice_list[i]))
        new_list.append(dice_list[x])
        
    result = [int(c.replace("d","")) for c in new_list]
         
    first_num = random.randint(1,result[0])   
    second_num = random.randint(1,result[1])  
    
    print("First dice rolled to {} and the second dice rolled to {}".format(first_num, second_num))
    
    final_result = first_num + second_num
    
    return final_result

def expand_dice(lst):    
    lst1 = []    
    for i in lst:
        i = i.strip()
        number = int(i[0])
        dice = i[1:]        
        
        for num in range(number):
            lst1.append (dice)
    return (lst1)    
    
lStr = input ("Input the list of dice: ").split(",")
expanded_List = expand_dice(lStr)
get_sum =  throw_dice(expanded_List)

print("Sum of 2 dice is {}".format(get_sum))

