#Capitalize a string
my_name = "kristofferson"
print(my_name.capitalize())

#Uppercase
print(my_name.upper())

#Starts With?
print(my_name.startswith("kris"))

print("\n")
#Endswith
print(my_name.endswith("son"))

print("\n")
#Find method
print(my_name.find("f", 7))

#loop through a string
for letter in my_name:
    print(letter)

print("\n")
#get the length of the string
length_of_string = len(my_name)
#loop through the string
for index in range(length_of_string):
    print(my_name[index])

print("\n")
sentence = "I have a dog. My dog is cute. Do you want a dog."

dog_count = 0

#loop
more_dogs = True
start_index = 0
while more_dogs:
    #find the first instance of dog
    found_index = sentence.find("dog", start_index)
    if found_index != -1:
        #increment dog_count by 1 #dog_count = dog_count + 1
        dog_count += 1       
        #update the index to the characheter after dog
        start_index = found_index + 1
    else:
        more_dogs = False

print(f"Number of Dogs: {dog_count}")

