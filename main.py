import usb.core
import usb.util
import random
import time

#connect to Digital Sound Level Meter
dev = usb.core.find(idVendor=0x64bd, idProduct=0x74e3)
print(dev)

if dev.is_kernel_driver_active(0):
    print("jo")
    dev.detach_kernel_driver(0)
usb.util.claim_interface(dev, 0)
if dev.is_kernel_driver_active(1):
    print("jup")
    dev.detach_kernel_driver(1)

#usb.util.claim_interface(dev, 1)


eout = dev[0][(0,0)][0]
ein  = dev[0][(0,0)][1]

STATE_REQUEST = bytearray([0xb3, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 0, 0, 0, 0])
#print(STATE_REQUEST)

#configuration = dev.get_active_configuration()

while True:
    ret = dev.write(eout.bEndpointAddress, STATE_REQUEST)
    #print(dev[0][(0,0)][0])

    data = dev.read(ein.bEndpointAddress, eout.wMaxPacketSize, timeout=10000)
    print(data)
    if len(data) > 0:
        print((data[0]*256 + data[1])/10)
    time.sleep(1)