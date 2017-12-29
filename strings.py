import random

def create_random_string(char_list):
    random.shuffle(char_list)
    return ''.join(char_list)
