import os
import time

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

def creat_if_exist(path : str):
    if  not os.path.exists(path):
        file = open('./project_root/logs/logfile.log','w', encoding = 'utf-8')
        file.writelines('Файл logfile.txt создан. ')
        file.writelines(time_file(path))
        file.close() 
    
 
def do_project_root():
    path = './project_root/logs/logfile.log' 
    do_if_exist("./project_root/logs")
    creat_if_exist(path)
    
def do_project(path: str):
     
    do_if_exist("./project_root/logs")
    creat_if_exist(path)

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

def do_files(path: str): 
    
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