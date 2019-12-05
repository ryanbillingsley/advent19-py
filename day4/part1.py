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

accepted = set()
for i in range(240298, 784956):
    digits = str(i)
    if not double_test.search(digits):
        continue
    if not check_increment(digits):
        continue
    accepted.add(i)

print(len(list(accepted)))
