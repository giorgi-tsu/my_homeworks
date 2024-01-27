## სავარჯიშო 3

# მორზეს ანბანის ფუნქციის გამოცხადება

def word_to_morse_code(word):
    
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--','?': '..--..', "'": '.----.',
        '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
        '&': '.-...',':': '---...', ';': '-.-.-.', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '$': '...-..-', '@': '.--.-.', ' ': '/'
    }

    morse_word = ""
    for char in word.upper():
        if char in morse_dict:
            morse_word += morse_dict[char] + " "
        else:
            return f"{char} is not in my morse dictionary, Sorry!"
    return morse_word.rstrip()


input_text = input("Enter text to morse-encode: ")

input_text_morse = word_to_morse_code(input_text)

with open("morse.txt", "a") as file:
    file.write(input_text_morse + "\n")

# შევამოწმოთ რა ჩაიწერა ფაილში
    
with open("morse.txt", "r") as file:
    print(file.read())