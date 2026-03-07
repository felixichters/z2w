# Overview

Configures a Raspberry Pi Zero 2W as a USB composite gadget exposing:
- **HID keyboard** — acts as a USB keyboard to the connected host
- **USB Ethernet (ECM)** — provides a network link

# Pi Setup

## 1. Enable the USB device controller

```bash
sudo bash gadget-setup/boot-setup.sh
```

This adds `dtoverlay=dwc2` to `/boot/firmware/config.txt`.

## 2. Install the gadget service

```bash
sudo bash gadget-setup/install-service.sh
```
gadget-setup.sh and install-service.sh both accept flags to disable individual functions:
```bash
--no-ethernet   # Disable USB Ethernet (ECM)
--no-hid        # Disable HID keyboard
```
This installs and enables a systemd service that runs `gadget-setup.sh` at boot, creating `/dev/hidg0` (HID keyboard) and `usb0` (Ethernet).

# HID Keystroke Payloads

Workflow: write a human-readable script → compile to binary → send.

## Script format (`.txt`)

```
# Comments with
WIN+r                # Key combo: hold Win, press R, release all
DELAY 500            # Wait 500ms
TYPE notepad         # Type literal text
ENTER                # Press and release a single key
CTRL+SHIFT+ESC       # Multi-modifier combo
```
**Named keys:** `A`–`Z`, `0`–`9`, `F1`–`F12`, `ENTER`, `ESC`, `BACKSPACE`, `TAB`, `SPACE`, `DELETE`, `HOME`, `END`, `PAGEUP`, `PAGEDOWN`, `UP`, `DOWN`, `LEFT`, `RIGHT`, `INSERT`, `PRINTSCREEN`, `CAPSLOCK`, `WIN`/`GUI`, `CTRL`, `SHIFT`, `ALT`, `ALTGR`, `MENU`

**Commands:**
| Command | Description |
|---------|-------------|
| `KEY` / `MOD+KEY` | Press combo and release |
| `TYPE <text>` | Type text character by character (layout-aware) |
| `DELAY <ms>` | Wait N milliseconds (max 65535) |

## Keyboard layouts

The `--layout` flag selects how `TYPE` characters are mapped to keycodes. Available layouts:

| Layout | Description |
|--------|-------------|
| `de` (default) | German QWERTZ — supports `äöüßÄÖÜ`, AltGr symbols (`@`, `€`, `{}`, `[]`, `\`, `~`, `\|`) |
| `us` | US QWERTY |

## Compile

```bash
python hid/generate-keycodes.py hid/examples/open-notepad.txt payload.bin --layout de
```

## Send from the Pi

```bash
python3 hid/send-keycodes.py ~/payload.bin
```