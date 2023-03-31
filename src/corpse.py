from config import Config

from textual.app import App

import logging
import pathlib
import sys


# establish default logging behaviour
logging.basicConfig(
    filename="corpseApp.log",
    encoding='utf-8',
    format='%(levelname)s :: %(asctime)s :: %(message)s',
    filemode='w',
    level=logging.DEBUG
)


class Corpse(App):
    """
    Corpse App
    """
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark


    


if __name__ == '__main__':
    config = Config()
    
    print(config.app_data_dir)