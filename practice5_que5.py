# 5) Write a program that takes an integer n and a filename as command line arguments 
#              and splits the file into multiple small files with each having n lines.



import sys
import os

def split_file_by_lines(input_filename, n):
    try:
        with open(input_filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    split_dir = "split_files"
    os.makedirs(split_dir, exist_ok=True)

    file_number = 1
    for i in range(0, len(lines), n):
        output_filename = f"{split_dir}/split_{file_number}.txt"
        with open(output_filename, 'w') as f:
            f.writelines(lines[i:i+n])
        file_number += 1

    print(f"File split complete! {file_number - 1} files created in the '{split_dir}' directory.")

if __name__ == "__main__":
   
        input_filename = str(input("Enter filename..."))
        n = int(input("Enter number of lines into which text to be splitted..."))
        split_file_by_lines(input_filename, n)
