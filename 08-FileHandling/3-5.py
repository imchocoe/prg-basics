###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input("Enter username")
password = input("Enter password")

# pattern (criteria) for username and password
username_pattern = '[a-z].......?'
password_pattern = '[a-z0-9_].........?'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match=re.match(password_pattern,password)

# print results
if username_match and password_match:
   print('correct')
else:
   print("incorrect")