import os
import sys
import random


def get_random_ints(k):
    int_list = []
    # check that k > 0
    if k > 0 :
        for i in range(0, k):
            int_list.append(random.randint(0, 255))
    else:
        return False
    return int_list
# END


def int_to_hex(int_list, prepend_0x=False):
    if(prepend_0x is True):
        return list(map(lambda x: '0x{:02x}'.format(x), int_list))
    else:
        return list(map(lambda x: '{:02x}'.format(x), int_list))
# END


def concat_list(list):
    return ''.join(list)

def list_to_upper(list):
    pass

def main():
    RANDOM_INTS = get_random_ints(16)
    print(RANDOM_INTS)
    # Convert Integers to hex format
    HEX_LIST = int_to_hex(RANDOM_INTS)
    print(HEX_LIST)
    # Concat hex strings
    print(concat_list(HEX_LIST))

    # uppercase - optional
    # print(list_to_upper(HEX_LIST))

if __name__ == '__main__':
    main()
