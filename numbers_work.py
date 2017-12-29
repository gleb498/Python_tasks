def check_different_n(numbers):
    for num in numbers:
        if numbers.count(num) > 1:
            return False
    return True


def delete_every_third_number(numbers):
    if not numbers:
        print('List is empty.')
    else:
        position = 3 - 1
        idx = 0
        len_list = (len(numbers))
        while len_list > 0:
            idx = (position + idx) % len_list
            print(numbers.pop(idx))
            len_list -= 1

