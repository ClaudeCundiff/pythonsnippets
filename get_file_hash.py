import hashlib
import os

def get_files(root_dir):
    f_bank = []
    if os.path.exists(root_dir) and os.path.isdir(root_dir):
        for root, dirs, files in os.walk(root_dir, topdown=True):
            for name in files:
                f = os.path.join(root, name)
                # print(f)
                f_bank.append(f)
            for name in dirs:
                d = os.path.join(root, name)
                # print(d)
    return f_bank

def do_file_hash(filename, BLOCK_SIZE = 65536):

    hasher = hashlib.sha256()
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCK_SIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCK_SIZE)
    return hasher.hexdigest()


if __name__ == '__main__':
    def main():
        r = '/root/PycharmProjects/playground/files'
        li = get_files(r)
        for i in li:
            print(do_file_hash(i))

    main()
