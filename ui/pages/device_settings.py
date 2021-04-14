from ui.ui_connection import UIConnection
from ui.selectors import SettingsSelectors
from ui.pages.about_phone_info_screen import AboutPhoneInfo


class Settings(UIConnection):

    def __init__(self, serial):
        super().__init__(serial)

        self.about_phone = AboutPhoneInfo(serial)

    @property
    def about_phone_button(self):
        return self.ui(**SettingsSelectors.ABOUT_PHONE_BUTTON)

    def click_about_phone_button(self):
        self.about_phone_button.click()

    def open_about_phone_info(self):
        if not self.about_phone_button.exists:
            self.ui(scrollable=True).scroll.to(self.about_phone_button)
        self.click_about_phone_button()
        return self.about_phone
