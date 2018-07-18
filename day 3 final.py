import pprint;
#def reset_game():
init1 = [(num,0) for num in range(0,3) ]
init2 = [(num,1) for num in range(0,3) ]
init3 = [(num,2) for num in range(0,3) ]
stuff = [init1,init2,init3]
#pp = pprint.PrettyPrinter(indent=4)
stuff.insert(10,stuff)
pp.pprint(stuff)
#reset_game()