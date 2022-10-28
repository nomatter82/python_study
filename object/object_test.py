
from animal import Animal
from Dog import Dog

Animal.hello()

print()

a = Animal(12)
b = Dog("멍", 5)

a.eat()
b.eat()

print()

a.get_age()
b.get_age()


print()

Animal.get_count()
Dog.get_count() 
