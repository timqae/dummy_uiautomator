from ppadb.client import Client as AdbClient


def get_serial():
    client = AdbClient(host='127.0.0.1', port=5037)
    device = client.devices()[0]
    return device.get_serial_no()


# first device serial connected via USB
DEVICE_SERIAL = get_serial()
