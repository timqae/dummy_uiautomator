import json
from device_serial import DEVICE_SERIAL
from ui.device_main_screen import MainScreen


if __name__ == '__main__':
    device = MainScreen(serial=DEVICE_SERIAL)

    device_info_json = json.dumps(device.ui.info, indent=4)
    print(device_info_json)

    print(device.ui.app_list_running())
