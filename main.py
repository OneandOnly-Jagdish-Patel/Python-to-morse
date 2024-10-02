# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for letter in text:
        if letter in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[letter])
        else:
            morse_code.append('?')
    return ' '.join(morse_code)

plain_text = input("Enter text to convert to Morse Code: ")

morse_text = text_to_morse(plain_text)

print("Morse Code:", morse_text)
