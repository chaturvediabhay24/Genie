import json
import importlib

def factory_import(module: str, function: str):
    try:
        module = importlib.import_module(module)
        function_or_class = getattr(module, function)
        return function_or_class
    except (ImportError, AttributeError, KeyError) as e:
        raise ImportError(f"Could not import {module}.{function}: {e}")


def write_file(file_path: str, data: dict):
    if not isinstance(data, (dict, list)):
        data=data.model_dump()
    
    if isinstance(data, list):
        data=[item.model_dump() if not isinstance(item, dict) else item for item in data ]

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    

def read_file(file_path: str):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data
    