#!/usr/bin/env python3
"""Play back a compiled HID binary file (.bin) via /dev/hidg0.

Usage: sudo python3 send-keycodes.py keycodes.bin [--device /dev/hidg0]
"""

import argparse
import struct
import sys
import time

HEADER = b'HID\x01'
REC_REPORT = 0x01
REC_DELAY = 0x02


def play(bin_path, device_path):
    with open(bin_path, 'rb') as f:
        header = f.read(4)
        if header != HEADER:
            print(f"Error: invalid header (expected HID\\x01, got {header!r})", file=sys.stderr)
            sys.exit(1)

        with open(device_path, 'wb') as dev:
            record_count = 0
            while True:
                rec_type = f.read(1)
                if not rec_type:
                    break  # EOF

                rec_type = rec_type[0]

                if rec_type == REC_REPORT:
                    report = f.read(8)
                    if len(report) < 8:
                        print("Error: truncated report record", file=sys.stderr)
                        sys.exit(1)
                    dev.write(report)
                    dev.flush()
                    record_count += 1

                elif rec_type == REC_DELAY:
                    delay_bytes = f.read(2)
                    if len(delay_bytes) < 2:
                        print("Error: truncated delay record", file=sys.stderr)
                        sys.exit(1)
                    ms = struct.unpack('>H', delay_bytes)[0]
                    time.sleep(ms / 1000.0)
                    record_count += 1

                else:
                    print(f"Error: unknown record type 0x{rec_type:02X}", file=sys.stderr)
                    sys.exit(1)

    print(f"Played {record_count} records from {bin_path}")


def main():
    parser = argparse.ArgumentParser(description='Send HID keystrokes from binary file')
    parser.add_argument('input', help='Input binary file (.bin)')
    parser.add_argument('--device', default='/dev/hidg0', help='HID gadget device (default: /dev/hidg0)')
    args = parser.parse_args()

    play(args.input, args.device)


if __name__ == '__main__':
    main()
