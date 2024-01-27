from plover.system.english_stenotype import *

KEYS =  ('T-', 'F-' , 'D-', 'M-', 'S-', 'R-', 'A-', 'O-', 'E-', 'U-')

IMPLICIT_HYPHEN_KEYS = ()
SUFFIX_KEYS = ()
NUMBERS = {}
NUMBER_KEY = None
FERAL_NUMBER_KEY = False
UNDO_STROKE_STENO = ""

KEYMAPS = {
    'Gemini PR': {
        "T-": ("T-", "-L"),
        "F-": ("K-", "-G"),
        "D-": ("P-", "-P"),
        "M-": ("W-", "-B"),        
        "S-": ("H-", "-F"),
        "R-": ("R-", "-R"),
        "A-": ("S1-", "-S"),
        "O-": ("S2-", "-T"),               
        "E-": ("O-", "-E"),
        "U-": ("A-", "-U")
        }
    }
