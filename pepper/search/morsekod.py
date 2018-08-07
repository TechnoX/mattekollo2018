morsekod = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}

text = input("Morsekod? ")

def rekurs(kvar, komb):
    if not kvar:
        print(komb + ", ", end="")
        return
    for morse, letter in morsekod.items():
        if kvar.startswith(morse):
            rekurs(kvar[len(morse):], komb + letter)
                
rekurs(text, "")
