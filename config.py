import yaml
from yaml.loader import SafeLoader

def files_with_transactions():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader = SafeLoader)
        
    return data["files_with_transactions"]

def amount_column_name():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader = SafeLoader)
        
    return data["column_names"]["amount_column"]

def date_column_name():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader = SafeLoader)
        
    return data["column_names"]["date_column"]

def transaction_name_column_name():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader = SafeLoader)
        
    return data["column_names"]["transaction_name_column"]

def transaction_names_to_ignore():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader = SafeLoader)

    items_as_str = list(map(str, data["transaction_names_to_ignore"]))
    return items_as_str

def transaction_positions_to_ignore():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader = SafeLoader)
        
    return data["transaction_positions_to_ignore"]

def export_configurations():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader = SafeLoader)
        
    return data["export"]