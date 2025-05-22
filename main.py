from project_12 import *
import os
import json

# task 1
path = './project_root/logs/logfile.log'
do_project_root()
do_project(path)
do_files(path)

# task 2
files_and_dirs = os.listdir('./project_root/data/row')
task_2(files_and_dirs)

# task 3

data_dir = './project_root/data/'
backups_dir = './project_root/backups/'
data_dir_= "./project_root/data_/"
backup_path = task_3_1(data_dir, backups_dir)
task_3_2(data_dir_, backup_path)


# task 4
path = './project_root/data/processed/'
files = os.listdir(path)

dict_json = {}
for file in files:  
    file_name = file
    absolute_path = os.path.abspath(os.path.join(path, file)) 
    file_size = os.path.getsize(os.path.join(path, file))
    file_time = time_file(os.path.join(path, file))
    d1 = FileInfo(file_name, absolute_path, file_size, file_time)
    print(d1)
    dict_json.update({file: d1.to_dict()})
    

with open('./project_root/output/FileInfo.json','w',encoding = 'utf-8') as file:
    json.dump(dict_json, file, ensure_ascii=False)
        
        
# import os
# import shutil
# import time
# import chardet
# import json
# import zipfile
# import hashlib
# from datetime import datetime


# def time_file(path: str): 
#     modification_time = os.path.getmtime(path)
#     readable_time = time.ctime(modification_time)
#     return f'Время: {readable_time} \n'
    
    
# def do_if_exist (path: str):
#     if os.path.exists(path):
#         return f'Попытка созднания, путь {path} существует. '
        
#     else:
#         os.makedirs(path)
#         return f'Папка создана {path}. '
 
 
# path = './project_root/logs/logfile.log' 
# do_if_exist("./project_root/logs")
# if  not os.path.exists(path):
#     file = open('./project_root/logs/logfile.log','w', encoding = 'utf-8')
#     file.writelines('Файл logfile.txt создан. ')
#     file.writelines(time_file(path))
#     file.close()

# with open('./project_root/logs/logfile.log','a', encoding = 'utf-8') as file:
#     file.writelines(do_if_exist("./project_root"))
#     file.writelines(time_file(path))
#     file.writelines(do_if_exist("./project_root/data/row"))
#     file.writelines(time_file(path))
#     file.writelines(do_if_exist("./project_root/data/processed"))
#     file.writelines(time_file(path))
#     file.writelines(do_if_exist("./project_root/logs"))
#     file.writelines(time_file(path))
#     file.writelines(do_if_exist("./project_root/backups"))
#     file.writelines(time_file(path))
#     file.writelines(do_if_exist("./project_root/output"))
#     file.writelines(time_file(path))

 

# with open('./project_root/logs/logfile.log','a', encoding = 'utf-8') as file_1:
#     with open('./project_root/data/row/data1.txt','w', encoding = 'utf-8') as file:
#         file.writelines("Файл созднан \n")
#         file.writelines("File is created \n")
#     file_1.writelines(f'файл data1.txt создан. ')
#     file_1.writelines(time_file(path))
#     with open('./project_root/data/row/data2.txt','w', encoding = 'CP1251') as file:
#         file.writelines("Файл созднан \n")
#         file.writelines("File is created \n")
#     file_1.writelines(f'файл data2.txt создан. ')
#     file_1.writelines(time_file(path))
    
# files_and_dirs = os.listdir('./project_root/data/row')
# dict_json = {}
# for file in files_and_dirs:    
#         #shutil.copy(f'./project_root/data/row/{file}',f'./project_root/data/processed{file}_processed')
#     d1 = {}
#     with open(f'./project_root/data/row/{file}', 'rb') as fl:
#         data = fl.read()
#         result = chardet.detect(data)
#         encoding = result['encoding']
#         name, ext = os.path.splitext(file)  # Разделяем имя и расширение
#         new_filename = f"{name}_processed{ext}"
#         with open(f'./project_root/data/processed/{new_filename}','w', encoding = encoding) as file_2:
#             decoded_data = data.decode(encoding)
#             processed_data = decoded_data.swapcase()
#             data_new = '\n'.join(' '.join(line.split()) for line in processed_data.splitlines())
                    
#             file_2.write(data_new)   
    
#             d1 = {"Имя файла": file, "Строки": data.decode(encoding), "Новое имя файла": new_filename, "Новые строки": data_new, \
#                    "Дата последнего изменения файла": time_file(f'./project_root/data/processed/{new_filename}'), \
#                       "Размер в байтах": os.path.getsize(f'./project_root/data/processed/{new_filename}')}
#             dict_json.update({file: d1})
# print(dict_json)
# with open('./project_root/output/processed_data.json','w',encoding = 'utf-8') as file:
#     json.dump(dict_json, file, ensure_ascii=False)

    
# data_dir = './project_root/data/'
# backups_dir = './project_root/backups/'
    
# os.makedirs(backups_dir, exist_ok=True)
    
#     # Формируем имя архива с текущей датой
# current_date = datetime.now().strftime('%Y%m%d')
# backup_filename = f'backup_{current_date}.zip'
# backup_path = os.path.join(backups_dir, backup_filename)
    
#     # Создаем ZIP-архив
# with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
#         # Рекурсивно обходим все файлы в data/
#     for root, dirs, files in os.walk(data_dir):
#         for file in files:
#             file_path = os.path.join(root, file)
#                 # Добавляем файл в архив, сохраняя относительный путь
#             arcname = os.path.relpath(file_path, start=data_dir)
#             backup_zip.write(file_path, arcname)
    
# print(f'Резервная копия успешно создана: {backup_path}')
    
# data_dir_= "./project_root/data_/"
# os.makedirs(data_dir_, exist_ok=True)
        
#         # Открываем архив
# with zipfile.ZipFile(backup_path, 'r') as backup_zip:
           
#             # Получаем список файлов в архиве
#     file_list = backup_zip.namelist()
#     print(f"Найдено {len(file_list)} файлов для восстановления")
            
#             # Восстанавливаем файлы
#     for file in file_list:
#                 # Извлекаем файл с сохранением структуры директорий
#         backup_zip.extract(file, data_dir_)
#         restored_path = os.path.join(data_dir_, file)
                
#                 # Проверяем целостность каждого файла
#         if not os.path.isdir(restored_path):
#             with open(restored_path, 'rb') as f:
#                 file_hash = hashlib.md5(f.read()).hexdigest()
#             with backup_zip.open(file) as zf:
#                 original_hash = hashlib.md5(zf.read()).hexdigest()
                
#                 if file_hash != original_hash:
#                    raise ValueError(f"Файл {file} поврежден при восстановлении")
            
#             print(f"Успешно восстановлено {len(file_list)} файлов в {data_dir_}")
         