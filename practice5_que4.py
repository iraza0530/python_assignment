# 4)  Write a programme to compute the number of python files (.py extension) in a specified directory recursively.


import os

def count_python_files(directory):
    count = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                count += 1

    return count

if __name__ == "__main__":
    current_directory = os.getcwd()

    # directory = '/Users/imran.khan/Documents/python/python_assignment'

    num_python_files = count_python_files(current_directory)
    print(f"Number of Python files (.py extension) in '{current_directory}': {num_python_files}")
   
