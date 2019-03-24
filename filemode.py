import sys
import os
import configparser
import re
import enum

# Character 	Meaning
# 'r' 	open for reading (default)
# 'w' 	open for writing, truncating the file first
# 'x' 	open for exclusive creation, failing if the file already exists
# 'a' 	open for writing, appending to the end of the file if it exists
# 'b' 	binary mode
# 't' 	text mode (default)
# '+' 	open a disk file for updating (reading and writing)

class FILE_MODE(enum.Enum):

    WRITE_TXT    = 'wt'
    READ_TXT     = 'rt'
    WRITE_BINARY = 'wb'
    READ_BINARY  = 'rb'

# END FILE_MODE

def main():
    for file_mode in FILE_MODE:
        print('{:15} = {}'.format(file_mode.name, file_mode.value))


if __name__ == '__main__':
    main()
