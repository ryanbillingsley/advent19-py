test_program = [1,9,10,3,2,3,11,0,99,30,40,50]
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
        return program

with open('day2.txt', 'r') as content_file:
    # Read in program from file, split on commas
    full_program = content_file.read().split(',')
    # Convert the list to ints
    full_program = [int(i) for i in full_program] 
    full_program[1] = 12
    full_program[2] = 2
    print(process_instruction(full_program)[0])