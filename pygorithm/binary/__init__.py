"""
Collection or binary conversions and algorithms
"""
from . import base2_to_base10
from . import base2_to_base16
from . import base2_to_ascii
from . import base10_to_base2
from . import base10_to_base16
from . import base16_to_base2
from . import base16_to_base10
from . import base16_to_ascii
from . import ascii_to_base2
from . import ascii_to_base16

__all__ = [
    'ascii_to_base2',
    'ascii_to_base16',
    'base2_to_base10',
    'base2_to_base16',
    'base2_to_ascii',
    'base10_to_base2',
    'base10_to_base16',
    'base16_to_base10',
    'base16_to_base2',
    'base16_to_ascii'
]
