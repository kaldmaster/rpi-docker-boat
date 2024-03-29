#
# Requires Bleak and dalybms packages installed to work
#
# https://pypi.org/project/bleak/
# pip install bleak
#
# https://pypi.org/project/dalybms/
# pip3 install dalybms
#

import asyncio
import logging
from dalybms import DalyBMSBluetooth

bms_mac = "96:69:08:01:05:08"

logging.basicConfig(filename='dalybms_connector_log.log', level=logging.DEBUG)

async def read_bms():
    print("read_bms:")
    bms = DalyBMSBluetooth()
    print("connecting to " + bms_mac)
    await bms.connect(bms_mac)
    print("connected, getting data... ")
    all_data = await bms.get_all()
    #mosfet_data = await bms.set_discharge_mosfet(True)
    print(all_data)
    await bms.disconnect()
    #print(mosfet_data)
    return all_data

asyncio.run(read_bms());