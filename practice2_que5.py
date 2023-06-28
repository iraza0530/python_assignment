## Write a programme to find out whether a given string is a valid regex or not.

import re
 
pattern = r"^[A-Za-z0-9]+$"
#pattern  = r"[.*"
 
try:
    re.compile(pattern)
    print("Given expression is a valid regex")
 
except re.error:
    print("The Pattern is not a valid regex expression.")
    exit()
