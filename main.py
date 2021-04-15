import json
import time

from utils.adb_device import device_serial, take_screenshot, get_device_build
from ui.pages.device_main_screen import MainScreen
from ui.kf_device.main_screen_kf import MainScreenKf

if __name__ == '__main__':
    device = MainScreen(serial=device_serial)

    print('Write Deviсe Info to the file')
    device_info_json = json.dumps(device.ui.device_info, indent=4)
    devices_build = get_device_build()
    with open('device_info.txt', 'a') as file:
        file.write(f'{device_info_json} \n')
        file.write(devices_build)

    print('Take Device Info screenshot')
    device.press_home_button()
    about_phone = device.open_notification_drawer().open_device_settings().open_about_phone_info().exist
    time.sleep(1)
    take_screenshot()

    # kf_device = MainScreenKf(serial=DEVICE_SERIAL)
    # hvac_panel = kf_device.open_hvac_panel()
    # hvac_panel.exists()
