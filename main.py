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
    dict_json.update({file: d1.to_dict()})
    

with open('./project_root/output/FileInfo.json','w',encoding = 'utf-8') as file:
    json.dump(dict_json, file, ensure_ascii=False)
        

with open('./project_root/output/FileInfo.json', 'r', encoding = 'utf-8') as file:
    loaded_data = json.load(file)
    
   
   
file_objects = {}
for filename, file_data in loaded_data.items():
    list_value = []
    for key, value in file_data.items():
        list_value.append(value)
          
    d2 = FileInfo(list_value[0], list_value[1], list_value[2], list_value[3])
    print(d2)
    file_objects.update({filename: d2})
    

# Файл для валидации (из предыдущего задания)
json_file_to_validate = './project_root/output/FileInfo.json'
    
    # Проводим валидацию
validation_result = validate_json(json_file_to_validate)
print(validation_result)