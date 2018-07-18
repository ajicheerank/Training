my_set = set()
while True:    
   str = input("Enter a word to add to the vocabulary: ") 
   
   if str == 'q':
       break
   elif str == 'v':
       print(" " .join(my_set))
   else:
       my_set.add(str)
       