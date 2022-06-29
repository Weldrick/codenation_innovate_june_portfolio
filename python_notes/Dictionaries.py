#dictionaries are encased using {}
#dictionaries have no referencable index

# pets = {"name": "Clouds",
#         "colour": "White",
#         "mood": "Whiney"}

cats = {"name" : "cat1", "colour" : "Blue", "mood" : "Sad"}
print(cats)
cats.update({"name" : "cat2", "colour" : "Red", "mood" : "Happy"})
print(cats)

#print(pets)
#print(pets[2]) #throws akey error
# print(pets["mood"]) #method of accessing data KEY
# print(pets["name"])
# print(f'My dog {pets["name"]} is in a {pets["mood"]} mood')
#annoted using single quotes to start and end the sentence 

#pets["mood"] = "hungry" #changes/updates values

#print(pets)
#methods that can be used for dictionaries = 
#print(pets.keys()) #dotnotation displays keys only
#pets["age"] = 2 #updates dictionary by adding age key
# print(pets.values())
# print(pets.items())

#find value by key
# print(pets.get("cat", "This key does not exist"))
# print(pets["cat"])

#using a list when printing presents data more efficiently
#print(pets.keys())
#print(list(pets.keys()))
#print(pets)

#clearest way to display information
#for i in pets.keys():
    #print(i)

#adding to a dictionary
#pets.update({"legs":"4"})
#pets.update({"name" : "Chickerin"})
#print(pets)

#remove from a dictionary
# pets.pop("mood")
# print(pets)