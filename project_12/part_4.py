import chardet

class FileInfo:
    def __init__(self, file_name, file_path, file_size, file_time):
        self.__file_name = file_name
        self.__file_path = file_path
        self.__file_size = file_size
        self.__file_time = file_time
        
    def __str__(self):
        return f'Имя файла {self.__file_name} Путь к файлу {self.__file_path} \
            Размер файла  {self.__file_size} Модификация в {self.__file_time} '
    
    
    def to_dict(self):
        return {
            "Имя файла": self.__file_name,
            "Путь к файлу": self.__file_path,
            "Размер файла": self.__file_size,
            "Модификация в": self.__file_time
        }