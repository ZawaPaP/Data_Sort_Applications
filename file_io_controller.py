def read_input_file_data(input_file):
    data = input_file.read()
    input_file.close()
    return data

def write_output_to_file(output_file, sortedList):
    for element in sortedList:
        output_file.write(str(element) + ",")
    output_file.write("\n")
    output_file.close()
