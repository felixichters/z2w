#!/bin/bash

modprobe libcomposite

cd /sys/kernel/config/usb_gadget/
mkdir -p pigadget
cd pigadget

echo 0x1d6b > idVendor   # linux foundation vid
echo 0x0104 > idProduct  # composite gadget pid
echo 0x0100 > bcdDevice  # v1.0.0
echo 0x0200 > bcdUSB     # usb 2.0

mkdir -p strings/0x409
echo "manufactur" > strings/0x409/manufacturer
echo "z2w" > strings/0x409/product
echo "237" > strings/0x409/serialnumber

mkdir -p configs/c.1/strings/0x409
echo "ethernet + keyboard" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower  

# ethernet
mkdir -p functions/ecm.usb0
echo "42:f2:97:74:b4:b8" > functions/ecm.usb0/host_addr
echo "42:f2:97:74:b4:b9" > functions/ecm.usb0/dev_addr

mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc

ln -s functions/ecm.usb0 configs/c.1/
ln -s functions/hid.usb0 configs/c.1/

#udevadm settle -t 5 || :
ls /sys/class/udc > UDC

# network
nmcli connection add type ethernet ifname usb0 con-name usb-gadget ipv4.method shared ipv6.method disabled || true
nmcli connection up usb-gadget || true
