#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend". Test. Test2.
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as file:
    friends = file.readlines()
    #print(friends)

for name in friends:
    with open("./Input/Letters/starting_letter.txt") as file:
        contents = file.read()
    stripped_name = name.strip()
    named_letter = contents.replace("[name]", stripped_name)

    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
        completed_letter.write(named_letter)
