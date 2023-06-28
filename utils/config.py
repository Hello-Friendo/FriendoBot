import os
import yaml


def load():

    config = []

    # Load yaml config
    if os.path.isFile("config.yaml"):
        with open("config.yaml", "r") as config:
            config = yaml.safe_load(config)

    if os.environ.get('server_id'):
        config['server_id'] = os.environ.get('server_id')

    if os.environ.get('server_id'):
        config['token'] = os.environ.get('server_id')

    config['log_file'] = os.environ.get('log_file', "bot")

    # Error Handling when discord:server_id doesn't exist
    if ("server_id" in config.keys() == False):
        print("[ERROR]: Config missing Discord server_id!")
        exit()

    # Error Handling when discord:token doesn't exist
    if ("token" in config.keys() == False):
        print("[ERROR]: Config missing Discord token!")
        exit()

    return config
