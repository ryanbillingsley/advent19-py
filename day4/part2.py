import re
import functools

double_test = re.compile(r'(\d)\1')

def check_increment(test_string):
    last_pos = ''
    for index, char in enumerate(test_string):
        if index == 0:
            last_pos = 0
            continue
        
        if int(char) < int(test_string[last_pos]):
            return False
        else:
            last_pos = index
    
    return True

# For a number like 112233
# Grab the first number 1
# Go to the second number, check if they are the same
# If they are the same number: 
# * increment the repeat counter
# * go to the next position
#
# if the next position is a different number
# * set a boolean indicating doubles exist
# * reset repeat counter
#
# if the next position is the same number
# * increment the repeat counter
# * when you finally hit a number that is different, then check if the repeat is % 2 

def double_test(test_string):
    last_pos = 0
    repeat_count = 0
    double_exists = False
    for index, char in enumerate(test_string):
        if index == 0:
            repeat_count += 1
            continue
        
        if char == test_string[last_pos]:
            repeat_count += 1
        else:
            # Different character, how many repeats were there?
            if repeat_count == 2:
                double_exists = True

            last_pos = index
            repeat_count = 1

    if repeat_count == 2:
        double_exists = True

    return double_exists

accepted = set()
for i in range(240298, 784956):
    digits = str(i)
    if not double_test(digits):
        continue
    if not check_increment(digits):
        continue
    accepted.add(i)

print(len(list(accepted)))

# print('112233', double_test(str(112233)))
# print('111122', double_test(str(111122)))
# print('123444', double_test(str(123444)))
# print('223444', double_test(str(223444)))