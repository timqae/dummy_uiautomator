import uiautomator2


class UIConnection:
    """
    Base class for all UI
    """
    def __init__(self, serial):
        self.serial = serial
        self.ui = uiautomator2.connect_usb(self.serial)
