key = ""
in_data = ""
while in_data == "":    
    in_data = input ("Please enter a coordinate-word pair in the format (x, y, word): ")
    list_1 = [int(x.strip()) for x in in_data.split(",")]    
    key = list_1([1,2])
    
print (key)
    