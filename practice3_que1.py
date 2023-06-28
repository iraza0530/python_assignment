import os
import filecmp  

files = os.listdir()


dup_file_name = str(input("Enter file name to find duplicate..."))
if_duplicate_found = False
for file in files:
    
   if file!=dup_file_name: 
    if filecmp.cmp(file,dup_file_name,False):
        if_duplicate_found = True
        print("Given file is duplicate to : ",file)


if if_duplicate_found == False:
    print("No duplicate file was found !!!")



