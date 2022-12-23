from ParseOptions import get_args
from SortController import SortController
from DataWriter import DataWriter

def main():
    args = get_args()
    print(args.sort)
    print(args.nums)
    print(args.infile)
    sorted_data = SortController(args).sortController()
    DataWriter(args).write(sorted_data)

if __name__ == "__main__":
    main()