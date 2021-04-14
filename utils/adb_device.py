from ppadb.client import Client as AdbClient


client = AdbClient(host='127.0.0.1', port=5037)


def get_serial() -> str:
    device = client.devices()[0]
    return device.get_serial_no()


# first device serial connected via USB
DEVICE_SERIAL = get_serial()

adb_device = client.device(DEVICE_SERIAL)


def take_screenshot():
    adb_device.shell("screencap -p /sdcard/device_info.png")
    adb_device.pull("/sdcard/device_info.png", "device_info.png")


def get_device_bluetooth_name():
    return adb_device.shell('getprop | grep "ro.build.fingerprint"')
