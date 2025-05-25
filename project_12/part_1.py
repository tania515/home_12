import os
import time

def time_file(path: str):        # время 
    modification_time = os.path.getmtime(path)
    readable_time = time.ctime(modification_time)
    return f'Время: {readable_time} \n'
   
    
def do_if_not_exist (path: str):    # создание папок
    if os.path.exists(path):
        return f'Попытка созднания, путь {path} существует. \n'
        
    else:
        os.makedirs(path)
        return f'Папка создана {path}. {time_file(path)}'

def creat_if_not_exist(path : str):    # создание  файла
    dir_path = os.path.dirname(path)
    do_if_not_exist(dir_path)
    if  not os.path.exists(path):  
        file = open(path,'w', encoding = 'utf-8')
        file.writelines(f'Файл {path} создан. ')
        file.writelines(time_file(path))
        file.close() 
    return f'Файл {path} создан. {time_file(path)}'
    
def log (path: str, mess: str):    # создание  файла
    try:
        with open(path,'a', encoding = 'utf-8') as file:
            file.writelines(mess)
        return True
    except FileNotFoundError:
        return(creat_if_not_exist(path))
      

    
def do_project(path: str):    

    with open(path,'a', encoding = 'utf-8') as file:
        path = "./project_root"
        file.writelines(do_if_not_exist("./project_root"))
        file.writelines(do_if_not_exist("./project_root/data/row"))
        file.writelines(do_if_not_exist("./project_root/data/processed"))
        file.writelines(do_if_not_exist("./project_root/logs"))
        file.writelines(do_if_not_exist("./project_root/backups"))
        file.writelines(do_if_not_exist("./project_root/output"))
     

def do_files(path: str): 
    
    with open(path,'a', encoding = 'utf-8') as file_1:
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