Replacement = "[name]"  #be able to replace string to different names

#open file invited_names
with open("./Input/Input/Names/invited_names.txt") as names:
    #creates list out of invited_names
    names = names.readlines()

#opens file starting_letter
with open("./Input/Input/Letters/starting_letter.txt") as letter:
    #reads starting_letter
    Original_letter = letter.read()

    #creates for loop to replace [name] with invited guest name
    for name in names:
        #removes the /n
        strip_name = name.strip()
        #creates new letter with strip_name
        new_letter = Original_letter.replace(Replacement, strip_name)
        #opens output folder to create finished letters of each invited guest name
        with open(f"./Output/Ready to send letters/letter_for_{strip_name}.txt", mode="w") as finished_letter:
            finished_letter.write(new_letter)