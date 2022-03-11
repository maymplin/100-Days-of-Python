#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

with open("Input/Names/invited_names.txt", "r") as file:
    names = [name.replace("\n", "") for name in file.readlines()]
    print(names)

for name in names:
    fin = open("Input/Letters/starting_letter.txt")
    out_file_path = f"Output/ReadyToSend/letter_for_{name}.txt"
    fout = open(out_file_path, "wt")

    for line in fin:
        if "[name]" in line:
            fout.write(line.replace("[name]", name))
        else:
            fout.write(line)

    fin.close()
    fout.close()



