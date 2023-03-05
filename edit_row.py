import os,csv
import constants as const  
import checkers

def modify_row(bd,id_key,field,new_value):
    """Получает на вход: адрес БД, ключ строки, имя поля к изменению, новое значение поля"""
    existing =[]
    with open(bd,'r',newline='', encoding='utf-8') as f:
        reader=csv.DictReader(f,delimiter='|')  
        headers=reader.fieldnames     
        for row in reader:
            existing.append(row)
        for row in existing:
            if row['id']==id_key:
                row[field]=new_value
                row['date']=checkers.timestamp()
    with open(bd,'w',newline='', encoding='utf-8') as f:    
        writer = csv.DictWriter(f,delimiter='|',fieldnames=headers)
        writer.writeheader()
        writer.writerows(existing)

    # with open(bd,newline='', encoding='utf-8') as f:
    #     input = open(bd, 'r',newline='')
    #     output = open('bd1.csv', 'w',newline='')
    #     writer = csv.writer(output,delimiter='|')
    #     headers=next(csv.reader(input,delimiter='|'))
    #     writer.writerow(headers)
    #     index_field_to_edit=(headers.index(field))
    #     for current_row in csv.reader(input,delimiter='|'):
    #         if current_row[0] == str(id_key):
    #             print(f'Подменяем {current_row[index_field_to_edit]} на {new_value}')
    #             current_row[index_field_to_edit]=new_value
    #         writer.writerow(current_row)
    #     input.close()
    #     output.close()
    # os.remove(const.DATA_BASE_NAME)
    # os.rename('bd1.csv', const.DATA_BASE_NAME)