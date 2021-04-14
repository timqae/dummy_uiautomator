from ui.ui_connection import UIConnection
from ui.pages.device_notification_drawer import NotificationDrawer


class MainScreen(UIConnection):

    def __init__(self, serial):
        super().__init__(serial)

        self.serial = serial
        self.notification_drawer = NotificationDrawer(serial)

    def press_home_button(self):
        self.ui.press('home')

    def open_notification_drawer(self):
        self.ui.open_notification()
        return self.notification_drawer
