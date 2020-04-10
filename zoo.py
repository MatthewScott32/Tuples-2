zoo = ("bear", "eagle", "wolf", "lion", "tiger", "snake", "cheetah", "T-Rex", "Shark", "Gorilla")
print(zoo.index("T-Rex"))

animal_to_find = "Gorilla"
if animal_to_find in zoo:
    print("animal found")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eigth_animal, ninth_animal, tenth_animal) = zoo
print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)

zoo_list = list(zoo)
print(zoo_list)
zoo_list.extend(["chimp"])
zoo_list.extend(["rabbit"])
zoo_list.extend(["duck"])
print(zoo_list)

zoo = tuple(zoo_list)
print(zoo)