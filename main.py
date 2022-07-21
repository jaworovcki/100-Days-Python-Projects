print("Welcome to the Band Name Generator!")
city = input("What's name of the city you grew up in?\n")
city_length = len(city)
pet = input("What's your pet's name?\n")
pet_length = len(pet)
band_length  = city_length + pet_length
print("Your band name could be "+city+" "+pet+" "+str(band_length))




