"""
https://adventofcode.com/2024/day/1

Time: 25 minutes
Issues:
- part 1
    - was not familiar with zip()
    - did not know that .sort works in place. do not used this in a return or to set a new value
    - file input: needed to remember how to setup reading the txt file of problem input.

- part 2 
    - did not read instructions properly for part2, mis understood how score was calculated.

"""
def write_lists(file):
    col1 = []
    col2 = []
    for line in open(file,'r'):
        vals = line.split()
        col1.append(float(vals[0]))
        col2.append(float(vals[1]))
    return col1, col2

def distance(col1, col2):
    col1.sort()
    col2.sort()
    dist = 0
    for val1, val2 in zip(col1, col2):
        dist = dist + abs(val2-val1)
    return dist

def part1(file):
    col1, col2 = write_lists(file)
    return distance(col1, col2)

def part2(file):
    col1, col2 = write_lists(file)


    count = unique_count(col2)

    score = 0
    for val in col1:
        if val in count:
            score = score + val * count[val]
    return score


def unique_count(arr):
    count = {}
    for val in arr:
        if val not in count:
            count[val] = 1
        else:
            count[val] = count[val] + 1
    return count
        

if __name__ == "__main__":
    # file = '2024/day1_ex.txt'
    file = '2024/day1.txt'
    print('part 1: ' +  str(part1(file)))
    print('part 2: ' + str(part2(file)))
