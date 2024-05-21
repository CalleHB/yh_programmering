#read funtions that read ou fil we input.
def read_file(file_path):
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

#write funtion that copyes the first file and prints a new one. 
def write_file(lines, file_path):
    
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print(f"Sucessfully writen to {file_path}.")


# user inputs
input_file_path = input("Enter the path of the input file: ")
output_file_path = input("Enter the path of the output file: ")

# read the content of the file
input_lines = read_file(input_file_path)

# write the content to the output file
write_file(input_lines, output_file_path)
