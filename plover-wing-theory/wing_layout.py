from plover.system.english_stenotype import *

KEYS =  ('S-', 'T-' , 'P-', 'K-', 'L-', 'R-', 'A-', 'O-', 'E-', 'U-')

IMPLICIT_HYPHEN_KEYS = ()
SUFFIX_KEYS = ()
NUMBERS = {}
NUMBER_KEY = None
FERAL_NUMBER_KEY = False
UNDO_STROKE_STENO = ""

KEYMAPS = {
    'Gemini PR': {
        "S-": ("T-", "-L"),
        "T-": ("K-", "-G"),
        "P-": ("P-", "-P"),
        "K-": ("W-", "-B"),        
        "L-": ("H-", "-F"),
        "R-": ("R-", "-R"),
        "A-": ("S1-", "-S"),
        "O-": ("S2-", "-T"),               
        "E-": ("O-", "-E"),
        "U-": ("A-", "-U")
        }
    }