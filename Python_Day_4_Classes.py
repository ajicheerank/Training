import random

class Die:
    def __init__(self, num_sides):
        if num_sides > 20:
            raise ValueError("You can't have more than a 20 sided die!")
        if num_sides % 2 != 0:
            raise ValueError("You can't have an odd-sided die")
        self._num_sides = num_sides 

    def roll(self):
        return random.randint(1, self._num_sides)

class Bag:
    def __init__(self, bag):
        self.bag = bag   

        lst = []
        for dice, cnt in self.bag.items():
            for num in range(cnt):
                lst.append (Die(dice))
        self.dice_list = lst  
        
       
    def draw (self, num_things):                                       
        new_list = []             
        for i in range(num_things):
            x = random.randint(1,len(self.dice_list)-1)
            new_list.append(self.dice_list[x])            
            self.dice_list.pop(x)                  
        return new_list
    
       
if __name__ == '__main__':
    b = Bag({4:1, 6:2, 8:4,10:2, 12:1, 20:3})
    set_aside = b.draw(3)       
    drawn = b.draw(2)    
    s = sum([Die.roll() for Die in drawn])
    print(s)

#It has: 1d4, 2d6, 4d8, 2d10, 1d12, 3d20. 