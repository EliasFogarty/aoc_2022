#input text file
my_file = "day_02_input.txt"

#score count
my_score = 0
my_score_p2 = 0

#open and read input file
with open(my_file) as file:
    my_lines = [lines.strip() for lines in file]

for i in range(0, len(my_lines)):
    
    my_play = my_lines[i].split(" ")
        
    if (my_play[0] == 'A'):
        if (my_play[1] == 'X'):
            my_score += 4
        elif (my_play[1] == 'Y'):
            my_score += 8
        elif (my_play[1] == 'Z'):
            my_score += 3
    elif (my_play[0] == 'B'):
        if (my_play[1] == 'X'):
            my_score += 1
        elif (my_play[1] == 'Y'):
            my_score += 5
        elif (my_play[1] == 'Z'):
            my_score += 9
    elif (my_play[0] == 'C'):
        if (my_play[1] == 'X'):
            my_score += 7
        elif (my_play[1] == 'Y'):
            my_score += 2
        elif (my_play[1] == 'Z'):
            my_score += 6
            
    if (my_play[0] == 'A'):
        if (my_play[1] == 'X'):
            my_score_p2 += 3
        elif (my_play[1] == 'Y'):
            my_score_p2 += 4
        elif (my_play[1] == 'Z'):
            my_score_p2 += 8
    elif (my_play[0] == 'B'):
        if (my_play[1] == 'X'):
            my_score_p2 += 1
        elif (my_play[1] == 'Y'):
            my_score_p2 += 5
        elif (my_play[1] == 'Z'):
            my_score_p2 += 9
    elif (my_play[0] == 'C'):
        if (my_play[1] == 'X'):
            my_score_p2 += 2
        elif (my_play[1] == 'Y'):
            my_score_p2 += 6
        elif (my_play[1] == 'Z'):
            my_score_p2 += 7

print(my_score)
print(my_score_p2)