# Write a Python function that prints all consecutive incremental numbers from a string of numbers.
# Example:
# Input: '588432347423122345'
# Output: '234', '23', '12', '2345'

def consecutive_inc_num(str_no):
    result = []
    mylist = []
    cur_no = ''

    for digit in str_no:
        if cur_no == '':
            cur_no = digit
        elif int(digit) == int(cur_no[-1]) + 1:
            cur_no += digit
        else:
            if len(cur_no) >= 2:
                result.append(cur_no)
            cur_no = digit

    if len(cur_no) >= 2:
        result.append(cur_no)

    for num in result:
        mylist.append(num)
    return mylist

# Example usage
str_no = '588432347423122345'
print(consecutive_inc_num(str_no))