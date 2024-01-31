with open(file="./Input/Names/invited_names.txt", mode="r") as names_file:
    # Saves the names in invited_names.txt as a list. Also includes "\n" notation:
    names_list = names_file.readlines()


# letter_string refers to the starting_letter.txt contents that were converted into a string:
with open(file="./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_string = letter_file.read()

    # this removes the "\n" notation from the names in names_list and assigns them to formatted_name variable:
    for name in names_list:
        formatted_name = name.replace("\n", "")

        # Replaces [name] placeholder in the STRING from starting_letter.txt to the specific name of the receiver.
        # The actual starting_letter.txt file remains unchanged.
        personalised_letter = letter_string.replace("[name]", formatted_name)

        # Creates an empty txt file for each person's letter in the ReadyToSend folder,
        # where the personalised letter contents are written inside the txt file.
        with open(file=f"./Output/ReadyToSend/{formatted_name}'s_letter.txt", mode="w") as personalised_letter_file:
            personalised_letter_file.write(personalised_letter)
