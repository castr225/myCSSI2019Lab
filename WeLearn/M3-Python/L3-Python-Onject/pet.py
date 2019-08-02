pet = {
"name": "Doggo",
"animal": "dog",
"species": "labrador",
"age": 5
}

class pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "happy"
    #pet is moving
    def move(self):
        print("> %s is walking..." % self.name)
        if self.is_moving:
            self.is_moving = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood = "fat & lazy"

    #pet is eating
    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood = "food coma"

my_pet1 = pet("fido", 3, "dog")
my_pet2 = pet("berro", 1, "dog")
my_pet3 = pet("kubo", 2, "dog")

print("My pet %s is %s years old" % (my_pet1.name, my_pet1.age))
print("My pet %s is %s year old" % (my_pet2.name, my_pet2.age))
print("My pet %s is %s years old" % (my_pet3.name, my_pet3.age))



#create a new pet
my_pet1 = pet("fido", 3, "dog")

my_pet1.is_hungry = True # manually set to True
print("is my pet hungry? %s" % my_pet1.is_hungry)
my_pet1.eat() #calls the eat method defined above
print("How about now? %s" % my_pet1.is_hungry)
print("My pet is feeling %s" % my_pet1.mood)

my_pet2 = pet("berro", 1, "dog")

my_pet2.is_moving = True # manually set to True
print("is my pet hungry? %s" % my_pet2.is_moving)
my_pet2.move() #calls the eat method defined above
print("How about now? %s" % my_pet2.is_moving)
print("My pet is feeling %s" % my_pet2.mood)
