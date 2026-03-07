#!/usr/bin/env python3
"""Compile a human-readable keystroke operations file (.txt) into a binary HID file (.bin).

Usage: python generate-keycodes.py input.txt output.bin [--layout de]
"""

import argparse
import struct
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layouts import load_layout

HEADER = b'HID\x01'
REC_REPORT = 0x01
REC_DELAY = 0x02
DEFAULT_INTER_KEY_DELAY = 20  # ms between characters in TYPE


def make_report(modifier_bits, keycode):
    """Build an 8-byte HID boot protocol keyboard report."""
    return struct.pack('BBBBBBBB', modifier_bits, 0x00, keycode, 0, 0, 0, 0, 0)


RELEASE_REPORT = make_report(0, 0)


def write_report(out, report):
    out.write(struct.pack('B', REC_REPORT))
    out.write(report)


def write_delay(out, ms):
    ms = min(ms, 65535)
    out.write(struct.pack('B', REC_DELAY))
    out.write(struct.pack('>H', ms))


def compile_combo(tokens, named_keys, modifier_keys, char_map):
    """Parse a key combo like ['CTRL', 'SHIFT', 'A'] into (modifier_bits, keycode)."""
    if len(tokens) == 1:
        name = tokens[0].upper()
        # Single token: could be a modifier pressed alone or a named key
        if name in modifier_keys and name not in named_keys:
            # Pure modifier (e.g., WIN alone) — send modifier with no keycode
            return modifier_keys[name], 0x00
        if name in named_keys:
            return 0x00, named_keys[name]
        # Try as single character
        if tokens[0] in char_map:
            return char_map[tokens[0]]
        raise ValueError(f"Unknown key: {tokens[0]}")

    # Multiple tokens: all but last are modifiers, last is the key
    mod_bits = 0
    for mod_name in tokens[:-1]:
        m = mod_name.upper()
        if m not in modifier_keys:
            raise ValueError(f"Unknown modifier: {mod_name}")
        mod_bits |= modifier_keys[m]

    key_name = tokens[-1]
    key_upper = key_name.upper()

    if key_upper in named_keys:
        keycode = named_keys[key_upper]
    elif key_name in char_map:
        char_mod, keycode = char_map[key_name]
        mod_bits |= char_mod
    else:
        raise ValueError(f"Unknown key: {key_name}")

    return mod_bits, keycode


def compile_file(input_path, output_path, layout_name):
    char_map, named_keys, modifier_keys = load_layout(layout_name)

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_path, 'wb') as out:
        out.write(HEADER)

        for lineno, raw_line in enumerate(lines, 1):
            # Strip comments
            line = raw_line.split('#', 1)[0].strip()
            if not line:
                continue

            try:
                if line.startswith('TYPE '):
                    text = line[5:]
                    for i, ch in enumerate(text):
                        if ch not in char_map:
                            raise ValueError(f"Character '{ch}' (U+{ord(ch):04X}) not in layout")
                        mod, keycode = char_map[ch]
                        write_report(out, make_report(mod, keycode))
                        write_report(out, RELEASE_REPORT)
                        if i < len(text) - 1:
                            write_delay(out, DEFAULT_INTER_KEY_DELAY)

                elif line.startswith('DELAY '):
                    ms = int(line[6:].strip())
                    if ms < 0 or ms > 65535:
                        raise ValueError(f"Delay out of range: {ms}")
                    write_delay(out, ms)

                else:
                    # Key combo: split on +
                    tokens = line.split('+')
                    tokens = [t.strip() for t in tokens]
                    mod_bits, keycode = compile_combo(tokens, named_keys, modifier_keys, char_map)
                    write_report(out, make_report(mod_bits, keycode))
                    write_report(out, RELEASE_REPORT)

            except ValueError as e:
                print(f"Error on line {lineno}: {e}", file=sys.stderr)
                print(f"  {raw_line.rstrip()}", file=sys.stderr)
                sys.exit(1)

    # Print summary
    size = os.path.getsize(output_path)
    print(f"Compiled {input_path} → {output_path} ({size} bytes, layout={layout_name})")


def main():
    parser = argparse.ArgumentParser(description='Compile keystroke operations to HID binary')
    parser.add_argument('input', help='Input operations file (.txt)')
    parser.add_argument('output', help='Output binary file (.bin)')
    parser.add_argument('--layout', default='de', help='Keyboard layout (default: de)')
    args = parser.parse_args()

    compile_file(args.input, args.output, args.layout)


if __name__ == '__main__':
    main()
