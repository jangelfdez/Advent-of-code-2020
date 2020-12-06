import numpy as np

people = 0
total_answers = 0
answers = np.array(np.zeros(26))


input_file = open("./Input/Day 6 - Custom customs - Data.txt", "r")
input_content = input_file.readlines()

for line in input_content:
  
  line = line.replace("\n", "")

  if (not line):
    answers = np.divide(answers, people)
    total_answers += np.shape(np.where(answers == 1.0))[1]
    answers = np.zeros(26)
    people = 0
  else :
    for letter in line :
      answers[ord(letter) - 97] += 1
    people += 1

answers = np.divide(answers,people)
total_answers += np.shape(np.where(answers == 1.0))[1]

print("\nA total of {} have been detected".format(total_answers))
  
  

 

