from config import Config
import logging

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Placeholder
from textual.containers import Container

from widgets.Recording import Recording
from widgets.Record import Record

# establish default logging behaviour
logging.basicConfig(
    filename="corpseApp.log",
    encoding='utf-8',
    format='%(levelname)s :: %(asctime)s :: %(message)s',
    filemode='w',
    level=logging.DEBUG,
    force=True
)


config = Config()


class Corpse(App):
    """
    Corpse App
    """

    TITLE = "Corpse"
    SUB_TITLE = "record audio"

    CSS_PATH = str(config.locations['css'])

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit Corpse")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        
        recording_p = [
            Recording(name=str(n+1) + " filename") for n in range(20)]

        # recordings container
        yield Container(*recording_p, classes="box", id="recordings")
        
        yield Container(
            Placeholder(id="info"),
            
            Container(
                Record(id="record"),
                Placeholder(id="live"),
                id="bottom"
            ),
            classes="box", id="main")


if __name__ == '__main__':
    app = Corpse()
    app.run()