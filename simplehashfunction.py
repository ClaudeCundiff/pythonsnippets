import sys
import os
import uuid
import pendulum


def get_utc_timestamp():
    return pendulum.now('UTC')
# end


def display_message(message):
    print('{} {}'.format(get_utc_timestamp(), message))
# end


def get_hash(x, mod):
    return x % mod
#end


def main():
    display_message('Starting...')

    H = {}
    H[0] = []
    H[1] = []
    H[2] = []

    TO_HASH = [1, 3, 4, 5, 6, 7, 8, 20]

    for i in TO_HASH:
        y = get_hash(i, 3)
        H[y].append(i)

    print(H)

    display_message('Done.')


if __name__ == '__main__':
    main()
