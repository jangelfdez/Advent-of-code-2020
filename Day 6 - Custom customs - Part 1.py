import numpy as np

answers = np.array(np.zeros(26))
total_answers = 0

input_file = open("./Input/Day 6 - Custom customs - Data.txt", "r")
input_content = input_file.readlines()

for line in input_content:
  
  line = line.replace("\n", "")

  if (not line):
    total_answers += int(np.sum(answers))
    answers = np.zeros(26)
  else :
    for letter in line :
      answers[ord(letter) - 97] = 1

total_answers += int(np.sum(answers))
print("A total of {} have been detected".format(total_answers))
  
  

 

