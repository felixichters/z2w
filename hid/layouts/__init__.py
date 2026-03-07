"""Layout loader: merges base US QWERTY with a layout overlay."""

import importlib
from . import _base


def load_layout(name):
    """Load a keyboard layout by name.

    Returns (char_map, named_keys, modifier_keys) where:
      - char_map: dict of character → (modifier_bits, keycode)
      - named_keys: dict of key name → keycode
      - modifier_keys: dict of modifier name → modifier bit
    """
    # Start with base US QWERTY
    char_map = dict(_base.CHAR_MAP)
    named_keys = dict(_base.NAMED_KEYS)
    modifier_keys = dict(_base.MODIFIER_KEYS)

    if name and name != 'us':
        overlay = importlib.import_module(f'.{name}', package=__name__)
        if hasattr(overlay, 'CHAR_MAP'):
            char_map.update(overlay.CHAR_MAP)
        if hasattr(overlay, 'NAMED_KEYS'):
            named_keys.update(overlay.NAMED_KEYS)
        if hasattr(overlay, 'MODIFIER_KEYS'):
            modifier_keys.update(overlay.MODIFIER_KEYS)

    return char_map, named_keys, modifier_keys
