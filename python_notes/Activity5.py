favSongs = [
    {"Artist" : "Kyuss", "SongName" : "One Inch Man", "Genre" : "Desert Rock", "Released" : "2006"},
    {"Artist" : "Primus", "SongName" : "To deft The Laws of Tradition", "Genre" : "Rock", "Released" : "2010"},
    {"Artist" : "Iron Butterfly", "SongName" : "In-A-Gadda-Da-Vida", "Genre" : "Rock", "Released" : "1968"}]

#print(list(favSongs)) #prints complete list
print(favSongs[0]) #prints 1st song in the list


#adds a new song to the list
favSongs.append({"Artist" : "Muke", "SongName" : "Surfs surfing", "Genre" : "Surf Rock", "Released" : "2020"})
print(favSongs)

 #removes a dictionary froma list
del(favSongs[2])
del(favSongs[0])
print(favSongs)
