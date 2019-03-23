import pathlib

def get_file_stem(path):
    p = pathlib.PurePath(path)
    return p.stem
# end 

if __name__ == '__main__':
    path = '/home/abjax/pycharm_projects/2019-03-18/schema.xml'
    print(get_file_stem(path))
