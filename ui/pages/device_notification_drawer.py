from ui.ui_connection import UIConnection
from ui.selectors import NotificationDrawerSelectors
from ui.pages.device_settings import Settings


class NotificationDrawer(UIConnection):

    def __init__(self, serial):
        super().__init__(serial)

        self.settings = Settings(serial)

    @property
    def settings_button(self):
        return self.ui(**NotificationDrawerSelectors.SETTINGS_BUTTON)

    def click_settings_button(self):
        button = self.settings_button
        if button.exists and button.info['clickable']:
            button.click()

    def open_device_settings(self):
        self.click_settings_button()
        return self.settings
