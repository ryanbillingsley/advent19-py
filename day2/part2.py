test_program = [1,9,10,3,2,3,11,0,99,30,40,50]
expected = 19690720
step = 0

def process_instruction(program, step = 0):
    start = step * 4
    end = step * 4 + 4
    instruction_set = program[start:end]
    opcode = instruction_set[0]
    arg1 = instruction_set[1]
    arg2 = instruction_set[2]
    result_addr = instruction_set[3]
    if opcode == 1:
        # Do addition
        program[result_addr] = program[arg1] + program[arg2]
        return process_instruction(program, step + 1)
    elif opcode == 2:
        # Do multiplacation
        program[result_addr] = program[arg1] * program[arg2]
        return process_instruction(program, step + 1)
    elif opcode == 99:
        return program[0]

def test_pair(pairs, full_program):
    test_program = full_program.copy()
    middle_point = len(pairs) // 2
    middle = pairs[middle_point]
    print(f'Middle: {middle} - {len(pairs)}')
    test_program[1] = middle[0]
    test_program[2] = middle[1]
    result = process_instruction(test_program)
    print(f'Result: {result} Expected: {expected}')

    if result == expected:
        return middle[0] * 100 + middle[1]
    elif result < expected:
        print('Result is less than expected')
        return test_pair(pairs[middle_point:], full_program)
    elif result > expected:
        print('Result is greater than expected')
        return test_pair(pairs[:middle_point], full_program)


with open('day2.txt', 'r') as content_file:
    # Read in program from file, split on commas
    full_program = content_file.read().split(',')
    # Convert the list to ints
    full_program = [int(i) for i in full_program] 

    pairs = []
    for x in range(100):
        for y in range(100):
            pairs.append((x, y))

    print(test_pair(pairs, full_program))
