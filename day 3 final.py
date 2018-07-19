def reset_game():
    init1 = [(num,0) for num in range(0,3) ]
    init2 = [(num,1) for num in range(0,3) ]
    init3 = [(num,2) for num in range(0,3) ]
    stuff = [init1,init2,init3]
    #pp = pprint.PrettyPrinter(indent=4)
    #stuff.insert(10,stuff)
    

    while True:
        str = input("where will you play?   ")
        if str != "":
            x = tuple([int(y) for y in str.split(",")])
            #print (x)
            for idx, value in enumerate(init1):      
                print (value,x)
                if value == x:                    
                    init1.pop(idx)
                    init1.insert(idx,"X")                    
                    break    
            for idx, value in enumerate(init2):      
                print (value,x)
                if value == x:                    
                    init1.pop(idx)
                    init1.insert(idx,"X")                    
                    break    
            for idx, value in enumerate(init3):      
                print (value,x)
                if value == x:                    
                    init1.pop(idx)
                    init1.insert(idx,"X")                    
                    break    
         
                
        else:
            break
        
       
reset_game()

#init1 = [(num,0) for num in range(0,3) ]
#y = "0,0"
#print (type(str))
#for idx,str in enumerate(init1):
#    print(idx,str)

#x = tuple([int(str) for str in y.split(",")])
#print(x)
