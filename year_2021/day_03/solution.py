from operator import gt, lt


class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = 0

    def add(self, input):
        self.data += 1
        if len(input) > 0:
            side = {"0": "left", "1": "right"}[input[0]]
            if not getattr(self, side):
                setattr(self, side, Tree())
            getattr(self, side).add(input[1:])

    def __repr__(self) -> str:
        return f"Tree <class data={self.data}>"

    def get_level_data(self, level=0, data_record={}):
        if self.right or self.left:
            if level not in data_record.keys():
                data_record[level] = {"left": 0, "right": 0}

            for side in ["left", "right"]:

                if getattr(self, side):
                    data_record[level][side] += getattr(self, side).data
                    getattr(self, side).get_level_data(level + 1, data_record)

        return data_record

    def search(self, default=1):
        if self.left or self.right:
            left = getattr(self.left, "data", 0 if default == 1 else 10000)
            right = getattr(self.right, "data", 0 if default == 1 else 10000)

            operation = gt if default == 1 else lt
            if operation(left, right):
                return "0" + self.left.search(default=default)

            if operation(right, left):
                return "1" + self.right.search(default=default)

            return str(default) + getattr(
                self, "right" if default == 1 else "left"
            ).search(default=default)
        return ""


def part_1(get_input):
    tree = Tree()
    for item in get_input():
        tree.add(item.strip())

    digit_counts = tree.get_level_data()

    digits = "".join(
        [
            "0" if digit_count["left"] > digit_count["right"] else "1"
            for digit_count in digit_counts.values()
        ]
    )
    inverse = "".join(["0" if digit == "1" else "1" for digit in digits])

    return int(digits, 2) * int(inverse, 2)


def part_2(get_input):
    tree = Tree()
    for item in get_input():
        tree.add(item.strip())

    oxygen_code = tree.search()
    co2_code = tree.search(default=0)

    return int(oxygen_code, 2) * int(co2_code, 2)
