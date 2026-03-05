#!/bin/bash
BOOT_CFG="/boot/firmware/config.txt"
echo "starting usb composite gadget setup..."

if ! grep -q "dtoverlay=dwc2" "$BOOT_CFG"; then
    echo "dtoverlay=dwc2" >> "$BOOT_CFG"
    echo "added dtoverlay=dwc2 to $BOOT_CFG"
else
    echo "dtoverlay=dwc2 already exists in $BOOT_CFG"
fi
echo "done."
