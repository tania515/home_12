import os
import zipfile
import hashlib
from datetime import datetime

# data_dir = './project_root/data/'
# backups_dir = './project_root/backups/'
# data_dir_= "./project_root/data_/"
    
def task_3_1(data_dir, backups_dir):
    
    os.makedirs(backups_dir, exist_ok=True)
        
        # Формируем имя архива с текущей датой
    current_date = datetime.now().strftime('%Y%m%d')
    backup_filename = f'backup_{current_date}.zip'
    backup_path = os.path.join(backups_dir, backup_filename)
        
        # Создаем ZIP-архив
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
            # Рекурсивно обходим все файлы в data/
        for root, dirs, files in os.walk(data_dir):
            for file in files:
                file_path = os.path.join(root, file)
                    # Добавляем файл в архив, сохраняя относительный путь
                arcname = os.path.relpath(file_path, start=data_dir)
                backup_zip.write(file_path, arcname)
        
    print(f'Резервная копия успешно создана: {backup_path}')
    return backup_path
        
   
def task_3_2(data_dir_, backup_path):
    
    os.makedirs(data_dir_, exist_ok=True)
            
            # Открываем архив
    with zipfile.ZipFile(backup_path, 'r') as backup_zip:
            
                # Получаем список файлов в архиве
        file_list = backup_zip.namelist()
        print(f"Найдено {len(file_list)} файлов для восстановления")
                
                # Восстанавливаем файлы
        for file in file_list:
                    # Извлекаем файл с сохранением структуры директорий
            backup_zip.extract(file, data_dir_)
            restored_path = os.path.join(data_dir_, file)
                    
                    # Проверяем целостность каждого файла
            if not os.path.isdir(restored_path):
                with open(restored_path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                with backup_zip.open(file) as zf:
                    original_hash = hashlib.md5(zf.read()).hexdigest()
                    
                    if file_hash != original_hash:
                        raise ValueError(f"Файл {file} поврежден при восстановлении")
                
                print(f"Успешно восстановлено {len(file_list)} файлов в {data_dir_}")
            
