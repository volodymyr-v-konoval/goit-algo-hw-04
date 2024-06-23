def total_salary(path:str) -> (int, float):
    """ 
    The function returns totall salary and midle salary
    from the file.
    """
    salarys = []
    try:
        with open(path, 'r', encoding='utf-8') as fl:
            while True:
                fl_reader = fl.readline()
                if not fl_reader:
                    break
                empl_salary = fl_reader.split(',')
                salarys.append(int(empl_salary[1].strip()))          
        return sum(salarys), int(sum(salarys)/len(salarys))
    except ValueError:
        print('Some values in your data file are wrong or missing!')
    except (FileNotFoundError, ZeroDivisionError):
        print('Your path is wrong, or file does not exists!')

if __name__ == '__main__':
    total, average = total_salary('sourse-for-task-1/employees_list.md')
    print(f'Total salary: {total}, Average salary: {average}')