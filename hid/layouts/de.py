"""German QWERTZ layout overrides.
"""

from . import _base as B

MOD_NONE  = B.MOD_NONE
MOD_SHIFT = B.MOD_SHIFT
MOD_ALTGR = B.MOD_ALTGR

# German QWERTZ character map overrides
# Only entries that differ from US QWERTY base
CHAR_MAP = {
    # Y/Z swap
    'y': (MOD_NONE, B.KEY_Z),
    'z': (MOD_NONE, B.KEY_Y),
    'Y': (MOD_SHIFT, B.KEY_Z),
    'Z': (MOD_SHIFT, B.KEY_Y),

    # Number row: unshifted = digits (same), shifted = different symbols
    # 1→!, 2→", 3→§, 4→$, 5→%, 6→&, 7→/, 8→(, 9→), 0→=
    '!': (MOD_SHIFT, B.KEY_1),
    '"': (MOD_SHIFT, B.KEY_2),
    # §: U+00A7 - common German symbol
    '§': (MOD_SHIFT, B.KEY_3),
    '$': (MOD_SHIFT, B.KEY_4),
    '%': (MOD_SHIFT, B.KEY_5),
    '&': (MOD_SHIFT, B.KEY_6),
    '/': (MOD_SHIFT, B.KEY_7),
    '(': (MOD_SHIFT, B.KEY_8),
    ')': (MOD_SHIFT, B.KEY_9),
    '=': (MOD_SHIFT, B.KEY_0),

    # Key right of 0 (US minus key 0x2D): ß and ?
    'ß': (MOD_NONE, B.KEY_MINUS),
    '?': (MOD_SHIFT, B.KEY_MINUS),

    # Key right of ß (US equal key 0x2E): ´ (acute accent, dead key) and ` (grave)
    '´': (MOD_NONE, B.KEY_EQUAL),
    '`': (MOD_SHIFT, B.KEY_EQUAL),

    # ü is on US [ key (0x2F)
    'ü': (MOD_NONE, B.KEY_LEFTBRACE),
    'Ü': (MOD_SHIFT, B.KEY_LEFTBRACE),

    # + is on US ] key (0x30), * is shifted
    '+': (MOD_NONE, B.KEY_RIGHTBRACE),
    '*': (MOD_SHIFT, B.KEY_RIGHTBRACE),

    # # is on US backslash key (0x31), ' is shifted
    '#': (MOD_NONE, B.KEY_BACKSLASH),
    "'": (MOD_SHIFT, B.KEY_BACKSLASH),

    # ö is on US semicolon key (0x33)
    'ö': (MOD_NONE, B.KEY_SEMICOLON),
    'Ö': (MOD_SHIFT, B.KEY_SEMICOLON),

    # ä is on US apostrophe key (0x34)
    'ä': (MOD_NONE, B.KEY_APOSTROPHE),
    'Ä': (MOD_SHIFT, B.KEY_APOSTROPHE),

    # ^ is on US grave key (0x35), ° is shifted
    '^': (MOD_NONE, B.KEY_GRAVE),
    '°': (MOD_SHIFT, B.KEY_GRAVE),

    # Comma and period same position, but shifted gives ; and :
    ',': (MOD_NONE, B.KEY_COMMA),
    ';': (MOD_SHIFT, B.KEY_COMMA),
    '.': (MOD_NONE, B.KEY_DOT),
    ':': (MOD_SHIFT, B.KEY_DOT),

    # - is on US slash key (0x38), _ is shifted
    '-': (MOD_NONE, B.KEY_SLASH),
    '_': (MOD_SHIFT, B.KEY_SLASH),

    # 102nd key (between left Shift and Z on ISO): < > |
    '<': (MOD_NONE, B.KEY_102ND),
    '>': (MOD_SHIFT, B.KEY_102ND),
    '|': (MOD_ALTGR, B.KEY_102ND),

    # AltGr combinations
    '@': (MOD_ALTGR, B.KEY_Q),
    '€': (MOD_ALTGR, B.KEY_E),
    '{': (MOD_ALTGR, B.KEY_7),
    '[': (MOD_ALTGR, B.KEY_8),
    ']': (MOD_ALTGR, B.KEY_9),
    '}': (MOD_ALTGR, B.KEY_0),
    '\\': (MOD_ALTGR, B.KEY_MINUS),
    '~': (MOD_ALTGR, B.KEY_RIGHTBRACE),
    'µ': (MOD_ALTGR, B.KEY_M),
}

# Named key overrides for German layout (Y/Z swap applies)
NAMED_KEYS = {
    'Y': B.KEY_Z,
    'Z': B.KEY_Y,
}
