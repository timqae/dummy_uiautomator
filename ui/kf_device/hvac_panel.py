from ui.ui_connection import UIConnection
from ui.selectors import HvacPanelPageSelectors


class HvacPanelPage(UIConnection):
    def __init__(self, serial):
        super().__init__(serial)

    @property
    def exists(self):
        return self.ui(**HvacPanelPageSelectors.HVAC_PANEL).exists
