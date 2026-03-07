#!/bin/bash
# Creates and enables a systemd service that sends a HID payload at boot.

set -e

PAYLOAD="/path/to/payload.bin"
SEND_SCRIPT="/path/to/send-keycodes.py"
DELAY_SECS=5

cat > /etc/systemd/system/hid-payload.service <<EOF
[Unit]
Description=HID Keystroke Payload
After=usb-gadget.service
Requires=usb-gadget.service

[Service]
Type=oneshot
ExecStartPre=/bin/sleep $DELAY_SECS
ExecStart=/usr/bin/python3 $SEND_SCRIPT $PAYLOAD
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable hid-payload.service
