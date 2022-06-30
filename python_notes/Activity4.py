#Dictionary of countries including their capital cities
countries = {"England" : "London", "France" : "Paris", "Germany" : "Berlin", "Spain" : "Madrid", "Italy" : "Rome"}
#print(countries)

#adds more countries to the dictionary(Norway & Japan)

countries.setdefault("Norway", "Oslo")
countries.setdefault("Japan", "Tokyo")
#this method uses the dot notation method


print(list(countries)) #A clean method of printing the countries(keys only)
#print(countries["Norway"]) #prints out keys that are associated with norway(capital)

#print(countries.keys()) #prints counties as a list (easy to read) BUT doesnt show values(capital cities)
#print(countries.values()) #prints the values(capital cities)

#updates dictionary (removes capital cities and replaces them with language)
countries.update({"England" : "English", "France" : "French", "Germany" : "German", "Spain" : "Spanish", "Italy" : "Italien", "Norway" : "Norwegian", "Japan" : "Japanese"})
print(countries)
