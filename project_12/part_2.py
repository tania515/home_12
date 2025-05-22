import os
import chardet
import json
from datetime import datetime
from .part_1 import time_file
    

def task_2(files_and_dirs: str):
      
    dict_json = {}
    for file in files_and_dirs:    
            
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