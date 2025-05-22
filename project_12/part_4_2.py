import json
from jsonschema import validate, ValidationError
from jsonschema.exceptions import SchemaError
from jsonschema import validate, Draft7Validator

FILE_INFO_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^.*$": {  # Любое имя файла в качестве ключа
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "path": {"type": "string", "format": "uri-reference"},
                "size": {"type": "integer", "minimum": 0},
                "time": {"type": "string", "format": "date-time"}
            },
            "required": ["name", "path", "size", "time"],
            "additionalProperties": False
        }
    },
    "additionalProperties": False
}   

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