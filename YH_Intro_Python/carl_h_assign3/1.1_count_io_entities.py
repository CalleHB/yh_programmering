import os

#funtion that count directories from out input
def count_directories(dir_path):
    dir_count = 0
    
    for dirnames in os.walk(dir_path):
        dir_count += 1
    return dir_count 

#funtion that count .py files from out input path
def count_py_files(dir_path):
    py_file_count = 0
    
    for py in os.listdir(dir_path):
        
        if py.endswith(".py"):
            py_file_count += 1
    return py_file_count


path_to_dir = str(input("Input path to count and .py files: ")) 
dir_count = count_directories(path_to_dir)
py_count = count_py_files(path_to_dir)

print(f"Directories in file path: {dir_count} .py files in file path: {py_count}")


