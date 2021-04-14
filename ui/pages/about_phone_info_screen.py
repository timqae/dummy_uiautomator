from ui.ui_connection import UIConnection
from ui.selectors import AboutPhoneSelectors


class AboutPhoneInfo(UIConnection):

    def __init__(self, serial):
        super().__init__(serial)

    @property
    def title(self):
        return self.ui(**AboutPhoneSelectors.TITLE)

    @property
    def exist(self):
        return self.title.exists()
