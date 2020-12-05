
tree_number = 0

input_file = open("./Input/Day 3 - Toboggan Trajectory - Data.txt", "r")
input_content = input_file.readlines()

number_lines = len(input_content)
number_columns = len(input_content[0])

add_x = 3
add_y = 1

current_x = add_x
current_y = add_y

while (current_y <= number_lines - 1):

    if (input_content[current_y][current_x] == "#"):
        tree_number += 1
    
    current_x += add_x
    current_y += add_y

    if (current_x >= number_columns - 1):
        current_x -= (number_columns - 1)

print("A total of {} trees has been found".format(tree_number))




