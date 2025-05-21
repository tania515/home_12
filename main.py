import os
import shutil

def do_if_exist (path: str):
    if os.path.exists(path):
        return f'Путь {path} существует. \n'
        
    else:
        os.makedirs(path)
        return f'Папка создана {path}. \n'
 
 
 
path = 'logfile.log'
if  not os.path.exists(path):
    file = open('logfile.log','w', encoding = 'utf-8')
    file.writelines('Файл logfile.txt создан \n')
    file.close()

with open('logfile.log','a', encoding = 'utf-8') as file:
    file.writelines(do_if_exist("./project_root"))
    file.writelines(do_if_exist("./project_root/data/row"))
    file.writelines(do_if_exist("./project_root/data/processed"))
    file.writelines(do_if_exist("./project_root/logs"))
    file.writelines(do_if_exist("./project_root/backups"))
    file.writelines(do_if_exist("./project_root/output"))

shutil.move('./logfile.log', "./project_root/logs")    

