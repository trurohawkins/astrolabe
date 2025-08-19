import os
import sys
import json

def load_solar_system(file_name):
    
    if not os.path.exists(file_name):
        print(f"File {file_name} does not exist")
        print(f"Current directory: {os.getcwd()}")
        return None
    
    file_size = os.path.getsize(file_name)
    if file_size == 0:
        print(f"File {file_name} is empty")
        return None
    
    try:
        with open(file_name, 'r') as file:
            solar_system = json.load(file)
        return solar_system

    except json.JSONDecodeError:
        print(f"Error parsing JSON in file {file_name}")
    except PermissionError:
        print(f"Error: Permission denied to read file {file_name}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

#print(load_solar_system())