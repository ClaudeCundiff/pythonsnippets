'''

'''
import os
import sys

def get_python_version():
    """

    :return:
    """
    major = sys.version_info.__getattribute__('major')
    minor = sys.version_info.__getattribute__('minor')
    micro = sys.version_info.__getattribute__('micro')
    return '{}.{}.{}'.format(major, minor, micro)


def main():


    print(get_python_version())


if __name__ == '__main__':
    main()
