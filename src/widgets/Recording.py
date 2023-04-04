from textual.widgets import Label, Static
from textual.app import ComposeResult

from widgets.TimeDisplay import TimeDisplay

import logging


class Recording(Static):
    """
    Recoding class holding widget logic for wav files
    """
    
    def on_click(self, event) -> None:
        logging.debug(event.x)
    
    def compose(self) -> ComposeResult:
        yield Label(self.name or "err", id="recording-label")
        yield TimeDisplay(id="recording-timedisplay")