"""This is task 3 from homework"""

from sys import argv
from pathlib import Path

if len(argv) > 1:
    path = Path(argv[1])
else:
    path = Path.cwd()

const = len(str(path).split('/'))

def painting(path):
    
    depth = len(str(path).split('/'))
    i = depth - const

    if path.exists():

        if i == 0:
            print(path.name)
        elif i == 1:
            print('|-', path.name)
        else:
            print('|' + ' '*i*2 + '|-',path.name)

        if path.is_dir():
            items = path.iterdir()
            for item in items:
                if item.is_dir() and not str(item.name).startswith('.'):
                    painting(item)
                else:
                    depth = len(str(item).split('/'))
                    i = depth - const

                    if i == 1:
                        print('|-', item.name)
                    else:
                        print('|' + ' '*i*2 + '|-', item.name)

if __name__ == '__main__':
    painting(path)
