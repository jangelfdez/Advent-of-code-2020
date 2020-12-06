import numpy as np
import pandas as pd
import re

input_file = open("./Input/Day 4 - Passport Processing - Data.txt", "r")
input_content = input_file.readlines()

passport_list = pd.DataFrame(np.zeros((300,8)), columns=['ecl','pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt', 'cid'])

passport_number = 0
valid_passport = 0

for passport in input_content:
  
  passport = passport.replace("\n", "")

  if (not passport):
    attributes_included = np.sum(passport_list.loc[passport_number,:])
    cid_value = passport_list.loc[passport_number,'cid']
    
    if ( attributes_included == 8 or
          ( attributes_included == 7 and cid_value ==0 ) ) :
      valid_passport += 1
    passport_number += 1

  else :
    regex = re.findall(r"(\S+):(\S+)", passport)

    for key_value in regex:
      passport_list.loc[passport_number, key_value[0]] = 1

if ( np.sum(passport_list.loc[passport_number,:]) == 8 or
      ( np.sum(passport_list.loc[passport_number,:]) == 7 and 
          passport_list.loc[passport_number,'cid'] == 0) ) :
  valid_passport += 1

print("\nA total of {} have been detected".format(valid_passport))
  
  

 

