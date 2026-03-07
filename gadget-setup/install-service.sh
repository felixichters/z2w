#!/bin/bash
set -e

ENABLE_ETH=1
ENABLE_HID=1

while [[ $# -gt 0 ]]; do
    case "$1" in
        --no-ethernet) ENABLE_ETH=0 ;;
        --no-hid)      ENABLE_HID=0 ;;
        *) echo "unknown option: $1"; exit 1 ;;
    esac
    shift
done

if [ "$ENABLE_ETH" -eq 0 ] && [ "$ENABLE_HID" -eq 0 ]; then
    echo "error: at least one of ethernet or hid must be enabled"
    exit 1
fi

GADGET_FLAGS=""
if [ "$ENABLE_ETH" -eq 0 ]; then GADGET_FLAGS="--no-ethernet"; fi
if [ "$ENABLE_HID" -eq 0 ]; then GADGET_FLAGS="--no-hid"; fi

if [ "$ENABLE_ETH" -eq 1 ] && [ "$ENABLE_HID" -eq 1 ]; then
    DESCRIPTION="USB Gadget Setup (HID + Ethernet)"
elif [ "$ENABLE_ETH" -eq 1 ]; then
    DESCRIPTION="USB Gadget Setup (Ethernet)"
else
    DESCRIPTION="USB Gadget Setup (HID)"
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GADGET_SCRIPT="/usr/local/bin/usb-gadget-setup.sh"
SERVICE_FILE="/etc/systemd/system/usb-gadget.service"

echo "installing usb gadget service..."

cp "$SCRIPT_DIR/gadget-setup.sh" "$GADGET_SCRIPT"
chmod +x "$GADGET_SCRIPT"
echo "installed gadget script to $GADGET_SCRIPT"

cat > "$SERVICE_FILE" <<EOF
[Unit]
Description=$DESCRIPTION
After=sysinit.target
Before=network.target

[Service]
Type=oneshot
ExecStart=$GADGET_SCRIPT $GADGET_FLAGS
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

echo "created $SERVICE_FILE"

systemctl daemon-reload
systemctl enable usb-gadget.service
echo "service enabled. it will start on next boot."
echo "to start now without rebooting, run: sudo systemctl start usb-gadget.service"
