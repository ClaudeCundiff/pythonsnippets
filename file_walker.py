'''
31c2dbb2e67188e37974b61ba3de791f
'''

import sys
import os


def file_walker(root_dir):
    file_list = []
    for root, dirs, files in os.walk(root_dir, topdown=True):
        for name in files:
            file_list.append(os.path.join(root, name))
        for name in dirs:
            os.path.join(root, name)
    return file_list
# end 


if __name__ == '__main__':
    root_path = '/root/PycharmProjects'

    # step 1: get list of files
    FILES = fire_walker(root_path)
    print('TOT_FILES: {}'.format(str(len(FILES))))


