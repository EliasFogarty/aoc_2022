#input text file
my_file = "day_03_input.txt"

#count
part_01 = 0
part_02 = 0

#elf group
elf = []
elf_count = 0

#open and read input file
with open(my_file) as file:
    my_lines = [lines.strip() for lines in file]

for i in range(0, len(my_lines)):

    sack = my_lines[i]
        
    #part_01
    
    half = len(sack) // 2
    
    intersect, = set(sack[:half]) & set(sack[half:])
        
    if intersect >= "a":
    
        part_01 += ord(intersect) - ord("a") + 1
        
    else:
    
        part_01 += ord(intersect) - ord("A") + 27
        
    #part_02
    
    elf.append(sack)
    elf_count += 1
    
    if elf_count == 3:

        intersect, = set(elf[0]) & set(elf[1]) & set(elf[2])
        
        if intersect >= "a":
        
            part_02 += ord(intersect) - ord("a") + 1
            
        else:
        
            part_02 += ord(intersect) - ord("A") + 27
        
        elf = []
        elf_count = 0
    
print(part_01)
print(part_02)
    