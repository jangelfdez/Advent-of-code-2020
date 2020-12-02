import re

valid_passwords = 0

input_file = open(".\Input\Day 2 - Password Philosophy - Data.txt", "r")
input_content = input_file.readlines()

for password in input_content:
  regex = re.search("^(\d+)-(\d+) (.): (\S+)", password)

  first_position = int(regex[1]) - 1
  second_position = int(regex[2]) - 1
  letter = regex[3]
  password_to_analyze = regex[4]

  if(password_to_analyze[first_position] == letter and password_to_analyze[second_position] != letter):
    valid_passwords +=1
  
  if(password_to_analyze[first_position] != letter and password_to_analyze[second_position] == letter):
    valid_passwords += 1

print("A total of {} passwords are valid".format(valid_passwords))
