import re

LONGEST_KEY = 40

all_entries = {										
	'' :      [	'',	'',	'a',	'A',	'o',	'O',	'',	'',	],
	'T' :     [	't',	'T',	'7',	'&',	'',	'',	'',	'',	],
	'F' :     [	'f',	'F',	'1',	'!',	'',	'',	'',	'',	],
	'D' :     [	'd',	'D',	'8',	'*',	'',	'',	'',	'',	],
	'M' :     [	'm',	'M',	'2',	'"',	'',	'',	'',	'',	],
	'TF' :    [	'k',	'K',	'4',	'$',	'',	'',	'',	'',	],
	'TD' :    [	'p',	'P',	'',	'',	'',	'',	'',	'',	],
	'TM' :    [	'v',	'V',	'',	'',	'',	'',	'',	'',	],
	'FD' :    [	'w',	'W',	'',	'',	'',	'',	'',	'',	],
	'FM' :    [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'DM' :    [	'n',	'N',	'5',	'%',	'',	'',	'',	'',	],
	'TFD' :   [	'q',	'Q',	'',	'',	'',	'',	'',	'',	],
	'TFM' :   [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TDM' :   [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FDM' :   [	'j',	'J',	'',	'',	'',	'',	'',	'',	],
	'TFDM' :  [	'b',	'B',	'',	'',	'',	'',	'',	'',	],
	'S' :     [	's',	'S',	'9',	'(',	'',	'',	'',	'',	],
	'TS' :    [	'\'',	'\"',	'',	'',	'',	'',	'',	'',	],
	'FS' :    [	'c',	'C',	'',	'',	'',	'',	'',	'',	],
	'DS' :    [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'MS' :    [	'-',	'_',	'',	'',	'',	'',	'',	'',	],
	'TFS' :   [	'x',	'X',	'',	'',	'',	'',	'',	'',	],
	'TDS' :   [	'z',	'Z',	'0',	')',	'',	'',	'',	'',	],
	'TMS' :   [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FDS' :   [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FMS' :   [	',',	';',	'',	'',	'',	'',	'',	'',	],
	'DMS' :   [	'u',	'U',	'',	'',	'',	'',	'',	'',	],
	'TFDS' :  [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TFMS' :  [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TDMS' :  [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FDMS' :  [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TFDMS' : [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'R' :     [	'r',	'R',	'3',	'£',	'',	'',	'',	'',	],
	'TR' :    [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FR' :    [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'DR' :    [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'MR' :    [	'l',	'L',	'',	'',	'',	'',	'',	'',	],
	'TFR' :   [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TDR' :   [	'.',	':',	'',	'',	'',	'',	'',	'',	],
	'TMR' :   [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FDR' :   [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FMR' :   [	'y',	'Y',	'',	'',	'',	'',	'',	'',	],
	'DMR' :   [	'e',	'E',	'',	'',	'',	'',	'',	'',	],
	'TFDR' :  [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TFMR' :  [	'=',	'+',	'',	'',	'',	'',	'',	'',	],
	'TDMR' :  [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FDMR' :  [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TFDMR' : [	')',	'(',	'>',	'<',	'',	'',	'',	'',	],
	'SR' :    [	'g',	'G',	'6',	'^',	'',	'',	'',	'',	],
	'TSR' :   [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FSR' :   [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'DSR' :   [	'h',	'H',	'',	'',	'',	'',	'',	'',	],
	'MSR' :   [	'/',	'\\',	'',	'',	'',	'',	'',	'',	],
	'TFSR' :  [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TDSR' :  [	'!',	'',	'',	'',	'',	'',	'',	'',	],
	'TMSR' :  [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FDSR' :  [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FMSR' :  [	'?',	'',	'',	'',	'',	'',	'',	'',	],
	'DMSR' :  [	'i',	'I',	'',	'',	'',	'',	'',	'',	],
	'TFDSR' : [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TFMSR' : [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TDMSR' : [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'FDMSR' : [	'',	'',	'',	'',	'',	'',	'',	'',	],
	'TFDMSR' :[	']',	'[',	'}',	'{',	'',	'',	'',	'',	],
}										
				
			
def lookup(strokes):
	output = ""

	for stroke_number, stroke in enumerate(strokes):
		if stroke_number == 0:
			if stroke != "FDMSR":
				raise KeyError
			if len(strokes) == 1:
				return "🦩"
		else:
			match = re.fullmatch(r'(T?F?D?M?S?R?)(O?)(A?)(E?)(U?)', stroke)
			entries = all_entries.get(match[1])
			index = 0
			if match[2] == "O":
				index += 4	
			if match[3] == "A":
				index += 2
			if match[4] == "E":
				index += 1
			if match[5] == "U":
				if stroke_number != len(strokes)-1:
					raise KeyError
			entry = entries[index]

			if entry == "":
				raise KeyError

			output += entry

	return output
