import os

#funtion to count all the lines of code in the user input folder
def count_py_lines(dir_path):
    total_lines = 0

    #go throue all the files and folders from the users.
    for entry in os.listdir(dir_path):
        full_path = os.path.join(dir_path, entry)

        if os.path.isdir(full_path):
            #If it is a folder, we go thouge it again(recursive)
            total_lines += count_py_lines(full_path)
        elif entry.endswith('.py'):
            #if the file ens with .py, we open it and read all the lines that are not empty.
            with open(full_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.strip():  # if the line is not empty we add one.
                        total_lines += 1

    return total_lines

#Askes for user input and user our funtion to read all the files.
input_file_path = input("Enter the path of the input file: ")
print("Python Line Count:", count_py_lines(input_file_path), "\nThats a lot of code!")
