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


# for initial load and subsequent resets
DEFAULT_CONFIG_FILE = {
    "locations": {
        "AppData": str(find_datadir()),
        "css": str(find_datadir() / 'app.css'),
        "recordings": str(find_datadir() / 'recordings'),
        "logs": str(find_datadir() / 'logs')
    }
}

DEFAULT_CSS = """
Corpse {
    layout: vertical
}
"""


class Config:
    """
    Config class
    handles application config logic
    """
    
    EXTENSION = '.toml'
    
    def __init__(self,) -> None:
        self.filename = "config" + self.EXTENSION
        self.app_data_dir = find_datadir()
        self.config: dict = {}
        
        self.load_config()
        self.locations = self.config['locations']
        
    def first_time_setup(self) -> None:
        """
        Initialize Corpse appdata
        """
        
        toml_str = toml.dumps(DEFAULT_CONFIG_FILE)
        self.config = toml.loads(toml_str)
        self.locations = self.config['locations']

        self.write_config()
        self.write_css(DEFAULT_CSS)
        
    def load_config(self) -> None:
        """
        load entire config file to dict
        """
        
        try:
            with open(self.app_data_dir / self.filename, 'r') as file:
                self.config = toml.load(file)
                
                # set string locations to Path objects
                a = Path(self.config['locations']['AppData'])
                self.config['locations']['AppData'] = a
                c = Path(self.config['locations']['css'])
                self.config['locations']['css'] = c
                r = Path(self.config['locations']['recordings'])
                self.config['locations']['recordings'] = r                
        except FileNotFoundError:
            self.first_time_setup()
        
    def write_config(self, mode: str = 'w') -> None:
        """
        write config dict to config file
        """
        
        with open(self.app_data_dir / self.filename, mode) as file:
            toml.dump(self.config, file)
            
    def write_css(self, css: str, mode: str = 'w') -> None:
        """
        write css to file

        Args:
            css (str): css to write
            mode (str, optional): write mode. Defaults to 'w'.
        """
        
        with open(self.locations['css'], mode) as file:
            file.write(css)