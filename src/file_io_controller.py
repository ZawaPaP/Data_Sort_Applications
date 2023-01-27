def read_input_file_data(input_file):
    data = input_file.readlines()
    input_file.close()
    return data

def write_output_to_file(output_file, sortedList):
    for x in sortedList:
        output_file.writelines(str(x)+'\n')
    output_file.close()
