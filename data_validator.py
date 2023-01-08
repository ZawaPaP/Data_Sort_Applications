import re
import sys

def validate_data(input_data):
    if not input_data:
        print("There is no input data")
        sys.exit(1)
    
    listed_data = __check_is_list(input_data)
    return __check_is_int(listed_data)

def __check_is_list(input_data):
    if isinstance(input_data, list):
        return input_data
    else:
        return __change_to_list(input_data)

    
def __change_to_list(input_data):   
    try:
        return re.split(",", input_data)
    except TypeError as e:
        print(e)
        print("unable to convert input data to list")

def __check_is_int(data):
    for i in range(len(data)):
        if not isinstance(data[i], int):
            try:
                data[i] = int(data[i])
            except TypeError as e:
                print(e)
                print("unable to convert input data to int type")
    return data
