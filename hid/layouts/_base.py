"""US QWERTY base mapping: character/key name → (modifier_bits, HID keycode).

Modifier bits (boot protocol):
  0x01 = Left Ctrl
  0x02 = Left Shift
  0x04 = Left Alt
  0x08 = Left GUI (Win)
  0x10 = Right Ctrl
  0x20 = Right Shift
  0x40 = Right Alt (AltGr)
  0x80 = Right GUI
"""

MOD_NONE  = 0x00
MOD_SHIFT = 0x02
MOD_ALTGR = 0x40

# HID Usage IDs (Keyboard/Keypad page 0x07)
KEY_A = 0x04
KEY_B = 0x05
KEY_C = 0x06
KEY_D = 0x07
KEY_E = 0x08
KEY_F = 0x09
KEY_G = 0x0A
KEY_H = 0x0B
KEY_I = 0x0C
KEY_J = 0x0D
KEY_K = 0x0E
KEY_L = 0x0F
KEY_M = 0x10
KEY_N = 0x11
KEY_O = 0x12
KEY_P = 0x13
KEY_Q = 0x14
KEY_R = 0x15
KEY_S = 0x16
KEY_T = 0x17
KEY_U = 0x18
KEY_V = 0x19
KEY_W = 0x1A
KEY_X = 0x1B
KEY_Y = 0x1C
KEY_Z = 0x1D
KEY_1 = 0x1E
KEY_2 = 0x1F
KEY_3 = 0x20
KEY_4 = 0x21
KEY_5 = 0x22
KEY_6 = 0x23
KEY_7 = 0x24
KEY_8 = 0x25
KEY_9 = 0x26
KEY_0 = 0x27
KEY_ENTER = 0x28
KEY_ESC = 0x29
KEY_BACKSPACE = 0x2A
KEY_TAB = 0x2B
KEY_SPACE = 0x2C
KEY_MINUS = 0x2D
KEY_EQUAL = 0x2E
KEY_LEFTBRACE = 0x2F
KEY_RIGHTBRACE = 0x30
KEY_BACKSLASH = 0x31
KEY_HASHTILDE = 0x32  # Non-US # and ~
KEY_SEMICOLON = 0x33
KEY_APOSTROPHE = 0x34
KEY_GRAVE = 0x35
KEY_COMMA = 0x36
KEY_DOT = 0x37
KEY_SLASH = 0x38
KEY_CAPSLOCK = 0x39
KEY_F1 = 0x3A
KEY_F2 = 0x3B
KEY_F3 = 0x3C
KEY_F4 = 0x3D
KEY_F5 = 0x3E
KEY_F6 = 0x3F
KEY_F7 = 0x40
KEY_F8 = 0x41
KEY_F9 = 0x42
KEY_F10 = 0x43
KEY_F11 = 0x44
KEY_F12 = 0x45
KEY_PRINTSCREEN = 0x46
KEY_SCROLLLOCK = 0x47
KEY_PAUSE = 0x48
KEY_INSERT = 0x49
KEY_HOME = 0x4A
KEY_PAGEUP = 0x4B
KEY_DELETE = 0x4C
KEY_END = 0x4D
KEY_PAGEDOWN = 0x4E
KEY_RIGHT = 0x4F
KEY_LEFT = 0x50
KEY_DOWN = 0x51
KEY_UP = 0x52
KEY_102ND = 0x64  # Non-US \ and | (key between left shift and Z on ISO)
KEY_MENU = 0x65

# Named key → HID keycode (used for combo parsing)
NAMED_KEYS = {
    'A': KEY_A, 'B': KEY_B, 'C': KEY_C, 'D': KEY_D, 'E': KEY_E,
    'F': KEY_F, 'G': KEY_G, 'H': KEY_H, 'I': KEY_I, 'J': KEY_J,
    'K': KEY_K, 'L': KEY_L, 'M': KEY_M, 'N': KEY_N, 'O': KEY_O,
    'P': KEY_P, 'Q': KEY_Q, 'R': KEY_R, 'S': KEY_S, 'T': KEY_T,
    'U': KEY_U, 'V': KEY_V, 'W': KEY_W, 'X': KEY_X, 'Y': KEY_Y,
    'Z': KEY_Z,
    '0': KEY_0, '1': KEY_1, '2': KEY_2, '3': KEY_3, '4': KEY_4,
    '5': KEY_5, '6': KEY_6, '7': KEY_7, '8': KEY_8, '9': KEY_9,
    'F1': KEY_F1, 'F2': KEY_F2, 'F3': KEY_F3, 'F4': KEY_F4,
    'F5': KEY_F5, 'F6': KEY_F6, 'F7': KEY_F7, 'F8': KEY_F8,
    'F9': KEY_F9, 'F10': KEY_F10, 'F11': KEY_F11, 'F12': KEY_F12,
    'ENTER': KEY_ENTER, 'RETURN': KEY_ENTER,
    'ESC': KEY_ESC, 'ESCAPE': KEY_ESC,
    'BACKSPACE': KEY_BACKSPACE,
    'TAB': KEY_TAB,
    'SPACE': KEY_SPACE,
    'DELETE': KEY_DELETE,
    'HOME': KEY_HOME,
    'END': KEY_END,
    'PAGEUP': KEY_PAGEUP,
    'PAGEDOWN': KEY_PAGEDOWN,
    'UP': KEY_UP,
    'DOWN': KEY_DOWN,
    'LEFT': KEY_LEFT,
    'RIGHT': KEY_RIGHT,
    'INSERT': KEY_INSERT,
    'PRINTSCREEN': KEY_PRINTSCREEN,
    'CAPSLOCK': KEY_CAPSLOCK,
    'MENU': KEY_MENU,
}

# Modifier name → modifier bit
MODIFIER_KEYS = {
    'CTRL': 0x01,
    'LCTRL': 0x01,
    'RCTRL': 0x10,
    'SHIFT': 0x02,
    'LSHIFT': 0x02,
    'RSHIFT': 0x20,
    'ALT': 0x04,
    'LALT': 0x04,
    'RALT': 0x40,
    'ALTGR': 0x40,
    'GUI': 0x08,
    'WIN': 0x08,
    'LGUI': 0x08,
    'LWIN': 0x08,
    'RGUI': 0x80,
    'RWIN': 0x80,
}

# Character → (modifier_bits, keycode) for US QWERTY
CHAR_MAP = {
    'a': (MOD_NONE, KEY_A), 'b': (MOD_NONE, KEY_B), 'c': (MOD_NONE, KEY_C),
    'd': (MOD_NONE, KEY_D), 'e': (MOD_NONE, KEY_E), 'f': (MOD_NONE, KEY_F),
    'g': (MOD_NONE, KEY_G), 'h': (MOD_NONE, KEY_H), 'i': (MOD_NONE, KEY_I),
    'j': (MOD_NONE, KEY_J), 'k': (MOD_NONE, KEY_K), 'l': (MOD_NONE, KEY_L),
    'm': (MOD_NONE, KEY_M), 'n': (MOD_NONE, KEY_N), 'o': (MOD_NONE, KEY_O),
    'p': (MOD_NONE, KEY_P), 'q': (MOD_NONE, KEY_Q), 'r': (MOD_NONE, KEY_R),
    's': (MOD_NONE, KEY_S), 't': (MOD_NONE, KEY_T), 'u': (MOD_NONE, KEY_U),
    'v': (MOD_NONE, KEY_V), 'w': (MOD_NONE, KEY_W), 'x': (MOD_NONE, KEY_X),
    'y': (MOD_NONE, KEY_Y), 'z': (MOD_NONE, KEY_Z),
    'A': (MOD_SHIFT, KEY_A), 'B': (MOD_SHIFT, KEY_B), 'C': (MOD_SHIFT, KEY_C),
    'D': (MOD_SHIFT, KEY_D), 'E': (MOD_SHIFT, KEY_E), 'F': (MOD_SHIFT, KEY_F),
    'G': (MOD_SHIFT, KEY_G), 'H': (MOD_SHIFT, KEY_H), 'I': (MOD_SHIFT, KEY_I),
    'J': (MOD_SHIFT, KEY_J), 'K': (MOD_SHIFT, KEY_K), 'L': (MOD_SHIFT, KEY_L),
    'M': (MOD_SHIFT, KEY_M), 'N': (MOD_SHIFT, KEY_N), 'O': (MOD_SHIFT, KEY_O),
    'P': (MOD_SHIFT, KEY_P), 'Q': (MOD_SHIFT, KEY_Q), 'R': (MOD_SHIFT, KEY_R),
    'S': (MOD_SHIFT, KEY_S), 'T': (MOD_SHIFT, KEY_T), 'U': (MOD_SHIFT, KEY_U),
    'V': (MOD_SHIFT, KEY_V), 'W': (MOD_SHIFT, KEY_W), 'X': (MOD_SHIFT, KEY_X),
    'Y': (MOD_SHIFT, KEY_Y), 'Z': (MOD_SHIFT, KEY_Z),
    '1': (MOD_NONE, KEY_1), '2': (MOD_NONE, KEY_2), '3': (MOD_NONE, KEY_3),
    '4': (MOD_NONE, KEY_4), '5': (MOD_NONE, KEY_5), '6': (MOD_NONE, KEY_6),
    '7': (MOD_NONE, KEY_7), '8': (MOD_NONE, KEY_8), '9': (MOD_NONE, KEY_9),
    '0': (MOD_NONE, KEY_0),
    '!': (MOD_SHIFT, KEY_1), '@': (MOD_SHIFT, KEY_2), '#': (MOD_SHIFT, KEY_3),
    '$': (MOD_SHIFT, KEY_4), '%': (MOD_SHIFT, KEY_5), '^': (MOD_SHIFT, KEY_6),
    '&': (MOD_SHIFT, KEY_7), '*': (MOD_SHIFT, KEY_8), '(': (MOD_SHIFT, KEY_9),
    ')': (MOD_SHIFT, KEY_0),
    ' ': (MOD_NONE, KEY_SPACE),
    '\n': (MOD_NONE, KEY_ENTER),
    '\t': (MOD_NONE, KEY_TAB),
    '-': (MOD_NONE, KEY_MINUS), '_': (MOD_SHIFT, KEY_MINUS),
    '=': (MOD_NONE, KEY_EQUAL), '+': (MOD_SHIFT, KEY_EQUAL),
    '[': (MOD_NONE, KEY_LEFTBRACE), '{': (MOD_SHIFT, KEY_LEFTBRACE),
    ']': (MOD_NONE, KEY_RIGHTBRACE), '}': (MOD_SHIFT, KEY_RIGHTBRACE),
    '\\': (MOD_NONE, KEY_BACKSLASH), '|': (MOD_SHIFT, KEY_BACKSLASH),
    ';': (MOD_NONE, KEY_SEMICOLON), ':': (MOD_SHIFT, KEY_SEMICOLON),
    "'": (MOD_NONE, KEY_APOSTROPHE), '"': (MOD_SHIFT, KEY_APOSTROPHE),
    '`': (MOD_NONE, KEY_GRAVE), '~': (MOD_SHIFT, KEY_GRAVE),
    ',': (MOD_NONE, KEY_COMMA), '<': (MOD_SHIFT, KEY_COMMA),
    '.': (MOD_NONE, KEY_DOT), '>': (MOD_SHIFT, KEY_DOT),
    '/': (MOD_NONE, KEY_SLASH), '?': (MOD_SHIFT, KEY_SLASH),
}
