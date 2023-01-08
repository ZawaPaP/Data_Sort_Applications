from parse_options import get_args
from sort import sort
from io_controller import IOController
from data_validator import validate_data
from utils import log


def main():
    log.configure_logging()
    args = get_args()
    io_controller = IOController(args)
    input_data = io_controller.get_input_data()
    validated_data = validate_data(input_data)
    sorted_data = sort(validated_data, args.sort_option)
    io_controller.output_data(sorted_data)

if __name__ == "__main__":
    main()
