def get_input_factory(filepath):
    def get_input():
        with open(filepath, "r") as input_file:
            for line in input_file:
                yield line.split()

    return get_input
