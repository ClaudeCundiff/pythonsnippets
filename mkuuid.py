import os
import uuid

def main():
    print('hi')
    u = uuid.uuid4()
    os.mkdir(str(u))
    os.chdir(str(u))
    os.mkdir('resources')
    os.mkdir('data')
    print('done.')


if __name__ == '__main__':
    main()
