import csv

def show_all_bd(db_name):
    """принимает на вход адрес БД
    выводит всю БД в консоль
    ничего не возвращает
    """
    with open(db_name,newline='', encoding='utf-8') as f:
        reader = csv.reader(f,delimiter='|')
        headers = next(reader)
        print(headers)
        for row in reader:
            print(row)