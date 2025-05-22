import os
import shutil
import time
import chardet
import json


def time_file(path: str): 
    modification_time = os.path.getmtime(path)
    readable_time = time.ctime(modification_time)
    return f'Время: {readable_time} \n'
    
    
def do_if_exist (path: str):
    if os.path.exists(path):
        return f'Попытка созднания, путь {path} существует. '
        
    else:
        os.makedirs(path)
        return f'Папка создана {path}. '
 
 
path = './project_root/logs/logfile.log' 
do_if_exist("./project_root/logs")
if  not os.path.exists(path):
    file = open('./project_root/logs/logfile.log','w', encoding = 'utf-8')
    file.writelines('Файл logfile.txt создан. ')
    file.writelines(time_file(path))
    file.close()

with open('./project_root/logs/logfile.log','a', encoding = 'utf-8') as file:
    file.writelines(do_if_exist("./project_root"))
    file.writelines(time_file(path))
    file.writelines(do_if_exist("./project_root/data/row"))
    file.writelines(time_file(path))
    file.writelines(do_if_exist("./project_root/data/processed"))
    file.writelines(time_file(path))
    file.writelines(do_if_exist("./project_root/logs"))
    file.writelines(time_file(path))
    file.writelines(do_if_exist("./project_root/backups"))
    file.writelines(time_file(path))
    file.writelines(do_if_exist("./project_root/output"))
    file.writelines(time_file(path))

 

with open('./project_root/logs/logfile.log','a', encoding = 'utf-8') as file_1:
    with open('./project_root/data/row/data1.txt','w', encoding = 'utf-8') as file:
        file.writelines("Файл созднан \n")
        file.writelines("File is created \n")
    file_1.writelines(f'файл data1.txt создан. ')
    file_1.writelines(time_file(path))
    with open('./project_root/data/row/data2.txt','w', encoding = 'CP1251') as file:
        file.writelines("Файл созднан \n")
        file.writelines("File is created \n")
    file_1.writelines(f'файл data2.txt создан. ')
    file_1.writelines(time_file(path))
    
files_and_dirs = os.listdir('./project_root/data/row')
dict_json = {}
for file in files_and_dirs:    
        #shutil.copy(f'./project_root/data/row/{file}',f'./project_root/data/processed{file}_processed')
    d1 = {}
    with open(f'./project_root/data/row/{file}', 'rb') as fl:
        data = fl.read()
        result = chardet.detect(data)
        encoding = result['encoding']
        name, ext = os.path.splitext(file)  # Разделяем имя и расширение
        new_filename = f"{name}_processed{ext}"
        with open(f'./project_root/data/processed/{new_filename}','w', encoding = encoding) as file_2:
            decoded_data = data.decode(encoding)
            processed_data = decoded_data.swapcase()
            data_new = '\n'.join(' '.join(line.split()) for line in processed_data.splitlines())
                    
            file_2.write(data_new)   
    
            d1 = {"Имя файла": file, "Строки": data.decode(encoding), "Новое имя файла": new_filename, "Новые строки": data_new, \
                   "Дата последнего изменения файла": time_file(f'./project_root/data/processed/{new_filename}'), \
                      "Размер в байтах": os.path.getsize(f'./project_root/data/processed/{new_filename}')}
            dict_json.update({file: d1})
print(dict_json)
with open('./project_root/output/processed_data.json','w',encoding = 'utf-8') as file:
    json.dump(dict_json, file, ensure_ascii=False)

    
            