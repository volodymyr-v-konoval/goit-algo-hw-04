import pprint


def get_cats_info(path:str) -> list:
    """
    The function makes a list of dicts from the file!
    """
    kays = ('id', 'name', 'age')
    final_list = []
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            while True:
                string = file.readline().strip()
                if not string:
                    break
                final_list.append(dict(zip(kays, string.split(','))))
        return final_list
    except FileNotFoundError:
        print('There is no such file or directory!')


if __name__ == '__main__':
    cats_info = get_cats_info('sourse-for-task-2/cats.md')
    pprint.pprint(cats_info)