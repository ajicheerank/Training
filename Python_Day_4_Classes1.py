class fish:
    def __init__(self,name, seaorfresh, lifespan, size):
        print("Creating an instance of fish with name {} ".format(name))
        self.name = name
        self.fish_type = seaorfresh
        self.lifespan = lifespan
        self.size = size
    
    def fish_name(self):
        print("Hello... my name is {} ".format(self.name))
        
    def fishtype(self):
        print ("I live in {} water".format(self.fish_type))
        
    def fish_life(self):
        print ("My lifespan is around {} years".format(self.lifespan))

    def fish_size(self):
        print ("Am a {} fish".format(self.size))
    
    def set_size(self, size):
        self.size = size
        
    def intro(self):
        print("Hello... Am a {name}. i live in {ftype} water. My life span is around {years}. And am {size} ".format(name=self.name, ftype=self.fish_type, years = self.lifespan, size = self.size))
        
    
  
my_fish = fish("Angel","Fresh", "4", "Small")

my_fish.intro()
my_fish.set_size("big")
my_fish.fish_size()
