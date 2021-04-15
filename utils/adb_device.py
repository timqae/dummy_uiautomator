from ppadb.client import Client as AdbClient


client = AdbClient(host='127.0.0.1', port=5037)
# get the first connected device serial
device_serial = client.devices()[0].get_serial_no()
adb_device = client.device(device_serial)


def take_screenshot():
    adb_device.shell("screencap -p /sdcard/device_info.png")
    adb_device.pull("/sdcard/device_info.png", "device_info.png")


def get_device_build():
    return adb_device.shell('getprop | grep "ro.build.fingerprint"')
