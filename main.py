import json
import time

from utils.adb_device import DEVICE_SERIAL, take_screenshot, get_device_bluetooth_name
from ui.pages.device_main_screen import MainScreen

if __name__ == '__main__':
    device = MainScreen(serial=DEVICE_SERIAL)

    print('Write devise info to the file')
    device_info_json = json.dumps(device.ui.info, indent=4)
    bt_name = get_device_bluetooth_name()
    with open('device_info.txt', 'a') as file:
        file.write(f'{device_info_json} \n')
        file.write(bt_name)

    print('Take Device Info screenshot')
    device.press_home_button()
    about = device.open_notification_drawer().open_device_settings().open_about_phone_info().exist
    time.sleep(1)
    take_screenshot()
