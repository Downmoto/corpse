import logging
import toml
import sys

from pathlib import Path


def get_datadir() -> Path:
    """
    returns a parent directory path
    where persistent application data can be stored.

    linux: ~/.local/share
    macOS: ~/Library/Application Support
    windows: C:/Users/<USER>/AppData/Roaming

    Returns:
        Path: path to cross platform application data directory
    """

    home = Path.home()
    ext = ""

    if sys.platform == "win32":
        ext = "AppData/Roaming"
    elif sys.platform == "linux":
        ext = ".corpse"
    elif sys.platform == "darwin":
        ext = "Library/Application Support"

    return home / ext

def find_datadir() -> Path:
    """
    locates the application data folder.
    creates application data folder on first launch

    Returns:
        Path: path to corpseApp app data directory
    """

    data_dir = get_datadir() / "corpseApp"

    if data_dir.exists():
        logging.info('app data directory found')
    else:
        Path(data_dir).mkdir(parents=True, exist_ok=True)

    return data_dir


DEFAULT_CONFIG_FILE = f"""
# Manually edit this file, or edit settings through application

[folder]
AppData = "{str(find_datadir)}"
"""

class Config:
    """
    Config class
    handles application config logic
    """
    
    EXTENSION = '.toml'
    
    def __init__(self,) -> None:
        self.filename = ".corpse" + self.EXTENSION
        self.app_data_dir = find_datadir()
        self.config: dict = {}
        
    def load_config(self) -> dict:
        """
        load entire config file to dict

        Returns:
            dict: dict representation of config file
        """
        
        with open(self.filename, 'r') as file:
            self.config = toml.load(file)
            return self.config
        
    def write_config(self, config: dict) -> None:
        """
        write config dict to config file

        Args:
            config (dict): dict representation of config file
        """
        
        with open(self.filename, 'w') as file:
            toml.dump(self.config, file)