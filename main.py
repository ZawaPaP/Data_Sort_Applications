from ParseOptions import get_args
from SortController import SortController
from DataWriter import DataWriter

def main():
    args = get_args()
    sorted_data = SortController(args).sortController()
    DataWriter(args).write(sorted_data)

if __name__ == "__main__":
    main()