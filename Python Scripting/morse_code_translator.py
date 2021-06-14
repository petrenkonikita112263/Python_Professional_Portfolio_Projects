# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


class MorseCodeTranslator:
    def __init__(self) -> None:
        super().__init__()

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, input_text):
        self.__text = input_text

    def encrypt_text(self) -> str:
        morse_code_text = ""
        for element in self.__text:
            if element != " ":
                morse_code_text += self.__text.replace(self.__text, MORSE_CODE_DICT[element.upper()])
            morse_code_text += " "
        return morse_code_text

    def decrypt_text(self, telegraph_msg: str) -> str:
        telegraph_msg += " "
        readable_text = ""
        citext = ""
        for letter in telegraph_msg:
            if letter != " ":
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    readable_text += " "
                else:
                    readable_text += list(MORSE_CODE_DICT
                                          .keys())[list(MORSE_CODE_DICT
                                                        .values()).index(citext)]
                    citext = ""
        return readable_text.lower()
