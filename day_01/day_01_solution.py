#input text file
my_file = "day_01_input.txt"

#output list
elf_list = []

#calories count
calories = 0

#open and read input file
with open(my_file) as file:
    my_lines = [lines.strip() for lines in file]

for i in range(0, len(my_lines)):
    
    if (my_lines[i] == ''):
    
        #add elf to list
        elf_list.append(calories)
        
        #reset calories
        calories = 0
        
    else :
    
        #add calories
        calories += int(my_lines[i])

#add last elf
elf_list.append(calories)

#sort high to low
elf_list.sort(reverse=True) 

#print elf list
print(elf_list)

#top elf
print(elf_list[0])

#top 3 elves
print(elf_list[0] + elf_list[1] + elf_list[2])