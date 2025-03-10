import json
import os

def load_config(config_path="config.json"):
    # Verifica se o arquivo de configuração existe
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        # Se o arquivo não existe, cria um arquivo com configurações padrão
        config = {
            "origin_path": "",
            "save_path": ""
        }
        # Salva o arquivo de configuração
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
    
    return config
