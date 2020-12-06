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
      if(key_value[0] == "byr"):
        value = int(key_value[1])
        if (value >= 1920 and value <= 2002):
          passport_list.loc[passport_number, key_value[0]] = 1

      if(key_value[0] == "iyr"):
        value = int(key_value[1])
        if (value >= 2010 and value <= 2020):
          passport_list.loc[passport_number, key_value[0]] = 1

      if(key_value[0] == "eyr"):
        value = int(key_value[1])
        if (value >= 2020 and value <= 2030):
          passport_list.loc[passport_number, key_value[0]] = 1

      if(key_value[0] == "hgt"):
        if("cm" in key_value[1]):
          value = int(key_value[1].replace("cm",""))
          if (value >= 150 and value <= 193):
            passport_list.loc[passport_number, key_value[0]] = 1
        if("in" in key_value[1]):
          value = int(key_value[1].replace("in",""))
          if (value >= 59 and value <= 76):
            passport_list.loc[passport_number, key_value[0]] = 1

      if(key_value[0] == "hcl"):
        regex = re.search(r"#[a-f0-9]{6}", key_value[1])
        if (regex != None):
          passport_list.loc[passport_number, key_value[0]] = 1
      
      if(key_value[0] == "ecl"):
        valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if ( key_value[1] in valid_colors and len(key_value[1]) == 3) :
          passport_list.loc[passport_number, key_value[0]] = 1

      if(key_value[0] == "pid"):
        regex = re.search(r"\d{9}", key_value[1])
        if (regex != None and len(key_value[1]) == 9):
          passport_list.loc[passport_number, key_value[0]] = 1
      
      if(key_value[0] == "cid"):
        passport_list.loc[passport_number, key_value[0]] = 1

if ( np.sum(passport_list.loc[passport_number,:]) == 8 or
      ( np.sum(passport_list.loc[passport_number,:]) == 7 and 
          passport_list.loc[passport_number,'cid'] == 0) ) :
  valid_passport += 1

print("\nA total of {} have been detected".format(valid_passport))
  
  

 

