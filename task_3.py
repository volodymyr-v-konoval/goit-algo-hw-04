"""
This is task 3 from homework.
Системні директорії з крапкою на початку,
обробляються як звичайні файли, оскільки вони містять
безліч файлів і вкладених директорій, і їх відображення 
робить вивід нечитабельним і мало корисним! На обробку 
такої директорії з відображенням як папки і без виклику
рекурсивної функції вже немає сил (бо цей код писався 3 дні!), 
а його реалізація не має нічого цікавого, всього лише ще
декілька циклів if...else!
"""

from sys import argv
from pathlib import Path
from colorama import Fore, Back, Style


if len(argv) > 1:
    path = Path(argv[1])
else:
    path = Path.cwd()

const = len(str(path).split('/'))

def painting(path: path) -> str:
    """I am allmost Da Vinchi! I paint a path!"""
    depth = len(str(path).split('/'))
    i = depth - const

    if path.exists():
        if i == 0:
            print(Back.BLUE + path.name + Style.RESET_ALL)
        elif i == 1:
            print('|-', Back.YELLOW + path.name + Style.RESET_ALL)
        else:
            print('|' + ' '*i*2 + '|-', Back.YELLOW + path.name + Style.RESET_ALL)
    else:
        print('Your path is wrong! Check it, please!')

    if path.is_dir():
        items = path.iterdir()
        for item in items:
            if item.is_dir() and not str(item.name).startswith('.'):
                painting(item)
            else:
                depth = len(str(item).split('/'))
                i = depth - const

                if i == 1:
                    print('|-', Fore.MAGENTA + item.name + Fore.RESET)
                else:
                    print('|' + ' '*i*2 + '|-', Fore.MAGENTA + item.name + Fore.RESET)

if __name__ == '__main__':
    painting(path)