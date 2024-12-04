"""
Total Time: 40 minutes

Issues:
- learning how enumerate works
    - enumerate(list[2:]) will return first idx as 0!!, not 2!!. should be obvious but did not work as expected
- found clever way to check (val1 * val2) > 0 if both have same sign


1 report per line
determine if safe / unsafe

safe:
- all increasing
- all decreasing
- any two adjacent levels differ by a least 1
- adjacent levels differe by a most 3
"""

def check_reports(file):
    safe = 0
    for line in open(file,'r'):
        line = line.split()
        line = [float(item) for item in line]
        safe = safe + is_safe(line)
    return safe

def is_safe(line):
    direction = line[1] - line[0]
    if direction == 0.0:
        return 0
    elif not (1 <= abs(direction) <= 3):
        return 0
    else:
        direction = direction / abs(direction)
    #skip first 2 
    for idx, val in enumerate(line[2:]):
        idx = idx+2
        delta = line[idx] - line[idx-1]
        if not (1 <= abs(delta) <= 3):
            return 0 # not safe, too big of jump
        if (delta / abs(delta)) * direction < 0:
            return 0 # not strictly increasing or decresaing
    return 1

def is_safe_damp(line):
    safe = is_safe(line)
    if safe:
        return 1

    for count, val in enumerate(line):
        new_line = line[:count] + line[count+1:] # test line sans 1 item
        safe = is_safe(new_line)
        if safe:
            return 1
    return 0

def part2(file):
    safe = 0
    for line in open(file,'r'):
        line = line.split()
        line = [float(item) for item in line]
        safe = safe + is_safe_damp(line)
    return safe

if __name__ == "__main__":
    # file = "2024/day2_ex.txt"
    file = "2024/day2.txt"

    print('part1: ' + str(check_reports(file)))
    print('part2: ' + str(part2(file)))
