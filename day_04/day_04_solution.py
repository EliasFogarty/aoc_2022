#input text file
my_file = "day_04_input.txt"

#count
part_1 = 0
part_2 = 0
my_range = []
my_sections = []

#open and read input file
with open(my_file) as file:
    my_pair = [lines.strip() for lines in file]

for i in range(0, len(my_pair)):

    #reset lists
    my_range.clear()
    my_sections.clear()
    
    #split pairs
    my_elf = my_pair[i].split(",")

    for j in range(2):
        #part_1
        my_range.append([eval(k) for k in my_elf[j].split("-")])
        
        #part_2
        my_sections.append(list(range(my_range[j][0],my_range[j][1]+1)))

    part_1 += ((my_range[0][0] <= my_range[1][0]) and (my_range[0][1] >= my_range[1][1])) or ((my_range[1][0] <= my_range[0][0]) and (my_range[1][1] >= my_range[0][1]))

    part_2 += (len(set(my_sections[0]) & set(my_sections[1])) >= 1)

print(part_1)
print(part_2)