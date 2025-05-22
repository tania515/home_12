import json
from jsonschema import validate, ValidationError
from jsonschema.exceptions import SchemaError
from jsonschema import validate, Draft7Validator
FILE_INFO_SCHEMA = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "FileInfo Dictionary",
  "description": "Словарь, где ключ — имя файла, а значение — объект FileInfo",
  "type": "object",
  "additionalProperties": {
    "type": "object",
    "properties": {
      "Имя файла": {
        "type": "string",
        "description": "Название файла"
      },
      "Путь к файлу": {
        "type": "string",
        "description": "Абсолютный или относительный путь к файлу"
      },
      "Размер файла": {
        "type": "number",
        "description": "Размер файла в байтах",
        "minimum": 0
      },
      "Модификация в": {
        "type": "string",
        "description": "Дата и время последнего изменения",
        "format": "date-time"
      }
    },
    "required": [
      "Имя файла",
      "Путь к файлу",
      "Размер файла",
      "Модификация в"
    ],
    "additionalProperties": False
  }
}

# FILE_INFO_SCHEMA = {
#     "type": "object",
#     "patternProperties": {
#          "type": "object",
#          "properties": {
#                 "name": {"type": "string"},
#                 "path": {"type": "string"},
#                 "size": {"type": "integer"},
#                 "time": {"type": "string", "format": "date-time"}
#             },
#             "required": ["name", "path", "size", "time"],
#             "additionalProperties": False
#         }
#     }

def validate_json(json_file):
    """
    Валидирует JSON файл против схемы
    Возвращает tuple: (bool - валиден ли, list - ошибки)
    """
    try:
               
        # Загружаем данные для проверки
        with open('./project_root/output/FileInfo.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
                # Валидируем данные
        validate(instance = data, schema = FILE_INFO_SCHEMA)
        return True, []
    
    except json.JSONDecodeError as e:
        return False, [f"Ошибка в формате JSON: {str(e)}"]
    except SchemaError as e:
        return False, [f"Ошибка в схеме: {str(e)}"]
    except ValidationError as e:
        errors = []
        validator = Draft7Validator(FILE_INFO_SCHEMA)
        for error in sorted(validator.iter_errors(data), key=str):
            errors.append(f"{error.json_path}: {error.message}")
        return False, errors
    except Exception as e:
        return False, [f"Неожиданная ошибка: {str(e)}"]