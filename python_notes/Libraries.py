#Libraries
import random #libraries go to top of page code reads from top to bottom
from random import random, randint #specifys a specific part from a libray

num1 = 0
num2 = 100
print(random.random()) #takes no arguments returns float between 0 and 1
print(random.uniform(num1, num2)) #returns float
print (random.randint(num1, num2)) #returns integer

