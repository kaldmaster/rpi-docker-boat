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
from dalybms import *

bms_mac = "96:69:08:01:05:08"

logging.basicConfig(filename='dalybms_connector_log.log', level=logging.DEBUG)

async def read_bms():
    bms = DalyBMSBluetooth()
    await bms.connect(bms_mac)
    all_data = await bms.get_all()
    #mosfet_data = await bms.set_discharge_mosfet(True)
    print(all_data)
    #print(mosfet_data)
    return all_data

asyncio.run(read_bms());