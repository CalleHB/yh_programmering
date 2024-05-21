import csv

#input variables from our users, what file thay want to use and where to sotr the new one
input_file_path = input("Input Mac address input file path:")
output_csv_path = input("Input Mac address output file path:")

#here i want a try go catch anything fault that can accure
try:
    with open(input_file_path, 'r') as input_file, open(output_csv_path, 'w', newline='') as output_file:#here i want to open the input file in read and the output file in write.
        csv_writer = csv.writer(output_file) # create a new objekt to write to
        csv_writer.writerow(['Mac addresses']) #add our first line to the new file.
        
        #read and write the old files content to the new file, like copy paste.
        for line in input_file: 
            csv_writer.writerow([line.strip()])

    print(f"Konvertering klar. CSV-filen sparad som '{output_csv_path}'.")

#errormassage if something gose wrong
except Exception as errorm:
    print(f"A problem accured: {errorm}")

