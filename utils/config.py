
import logging
import yaml
import os

def load():    
    # Error Handling, what if config.yaml doesn't exist?
    if(os.path.isfile("config.yaml") == False):
        print("[ERROR]: 'config.yaml' does not exist!")
        exit()

    # Load yaml config
    with open("config.yaml", "r") as config:
        config = yaml.safe_load(config)

    # Error Handling when discord:server_id doesn't exist
    if("server_id" in config['discord'].keys() == False):
        print("[ERROR]: Config missing Discord server_id!")
        exit()

    # Error Handling when discord:token doesn't exist
    if("token" in config['discord'].keys() == False):
        print("[ERROR]: Config missing Discord token!")
        exit()
        
    return config
