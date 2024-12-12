
INPUT = 'inputs/two.txt'

def part_one():
    safe_reports = 0
    with open(INPUT, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            line = line.split(' ')
            line = [int(x) for x in line]
            safe_reports += 1
            increasing = True
            if line[0] > line[1]:
                increasing = False
            for i in range(0, len(line) - 1):
                if increasing:
                    if line[i] > line[i + 1]:
                        safe_reports -= 1
                        break
                else:
                    if line[i] < line[i + 1]:
                        safe_reports -= 1
                        break
                if not (1 <= abs(line[i] - line[i + 1]) <= 3):
                    safe_reports -= 1
                    break

    return safe_reports

def safe_report(line):
    increasing = True
    if line[0] > line[1]:
        increasing = False
    for i in range(0, len(line) - 1):
        if increasing:
            if line[i] > line[i + 1]:
                return False
        else:
            if line[i] < line[i + 1]:
                return False
        if not (1 <= abs(line[i] - line[i + 1]) <= 3):
            return False
    return True

def part_two():
    safe_reports = 0
    with open(INPUT, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            line = line.split(' ')
            report = [int(x) for x in line]
            if safe_report(report):
                safe_reports += 1
            else:
                for i in range(0, len(report)):
                    mod_report = report[:i] + report[i + 1:]
                    if safe_report(mod_report):
                        safe_reports += 1
                        break
    return safe_reports






    return safe_reports
