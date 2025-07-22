import json


class Configuration:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            with open("config.json", "r") as f:
                cls._config = json.load(f)
        return cls._instance

    def get_config(self):
        return self._config


def load_config():
    return Configuration().get_config()
