import sys
sys.path.append('../')

from textual.widgets import Static, Button, Input
from textual.app import ComposeResult

from TimeDisplay import TimeDisplay

import audio

import logging
import datetime
import threading


class Record(Static):
    """
    Recoding class holding widget logic for wav files
    """      

    def on_click(self, event) -> None:
        logging.debug(event.x)
        
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        time_display = self.query_one(TimeDisplay)
        if button_id == "record-btn":
            time_display.start()
            self.add_class("started")
        elif button_id == "pause-record-btn":
            time_display.stop()
            self.remove_class("started")
        elif button_id == "stop-record-btn":
            time_display.reset()

    def compose(self) -> ComposeResult:
        yield TimeDisplay(id="record-timedisplay")
        yield Button("record", id="record-btn", variant="success")
        yield Button("stop", id="stop-record-btn", variant="error")
        yield Button("pause", id="pause-record-btn")
        yield Input(placeholder="File name", id="record-input")
