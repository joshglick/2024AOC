
INPUT = 'inputs/one.txt'

def part_one():
    left = []
    right = []
    with open(INPUT, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            output = line.split('   ')
            left.append(output[0])
            right.append(output[1])

    left = sorted(left)
    right = sorted(right)

    distance = 0
    for i in range(len(left)):
        distance += abs(int(left[i]) - int(right[i]))

    return distance

def part_two():
    return 0
