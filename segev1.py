class Animal(object):
    def __init__(self,sound,name,age,favorit_color):
        self.sound=sound
        self.name=name
        self.age=age
        self.favorit_color = favorit_color
    def eat(self,food):
        print(" yummyyyyyyy!!"+ self.name +" is eating"+food)
    def description(self):
        print (self.name+ " is "+ str(self.age) +" years old and loves the color "+ self.favorit_color)

    def make_sound(self,sound):
        self.sound("ooooooouuuuaaaaarrrhhhh")
        
        
j=Animal("oooouuuuaaarrrhhhhhhhh","Lion",23,"green")
j.eat("fish")
j.description()
j.make_sound


