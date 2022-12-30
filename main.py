from ParseOptions import get_args
from SortController import sortController
from DataOrganizer import DataOrganizer
from DataWriter import DataWriter

import sys
def main():
    args = get_args()
    organizer = DataOrganizer(args)
    data = organizer.data_validate()
    sort_type = args.sort
    sorted_data = sortController(data, sort_type)
    DataWriter(args).write(sorted_data)

if __name__ == "__main__":
    main()