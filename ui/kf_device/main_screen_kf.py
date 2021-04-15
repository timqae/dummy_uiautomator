from ui.ui_connection import UIConnection
from ui.selectors import MainScreenKingfisherSelectors
from ui.kf_device.hvac_panel import HvacPanelPage


class MainScreenKf(UIConnection):

    def __init__(self, serial):
        super().__init__(serial)

        self.hvac_panel = HvacPanelPage(serial)

    @property
    def hvac_button(self):
        return self.ui(**MainScreenKingfisherSelectors.HVAC_BUTTON)

    def click_hvac_button(self):
        self.hvac_button.click()

    def open_hvac_panel(self):
        self.click_hvac_button()
        return self.hvac_panel
