key,value = "",""
my_dict = {}
while True:    
    in_data = input ("Please enter a coordinate-word pair in the format (x, y, word): ")
    if in_data !="":
        list_1 = [x.strip() for x in in_data.split(",")]    
        key = ",".join (list_1 [0:2])
        value = list_1[2]    
        my_dict[key] = value
    else:
        break

while True:    
        in_input = input ("Please enter a coordinate to look up: ")
        if in_input != 'q':
            print(my_dict.get(in_input,"no data"))
        else:
            break