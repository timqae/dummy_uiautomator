from ui.ui_connection import UIConnection


class MainScreen(UIConnection):

    def __init__(self, serial):
        super().__init__(serial)

        self.serial = serial

