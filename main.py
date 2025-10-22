#Name of the app
print("""\n\nooo        ooooo                                                                                            .o8                     
`88.       .888'                                                                                           "888                     
 888b     d'888   .ooooo.  oooo d8b  .oooo.o  .ooooo.        .ooooo.  ooo. .oo.    .ooooo.   .ooooo.   .oooo888   .ooooo.  oooo d8b 
 8 Y88. .P  888  d88' `88b `888""8P d88(  "8 d88' `88b      d88' `88b `888P"Y88b  d88' `"Y8 d88' `88b d88' `888  d88' `88b `888""8P 
 8  `888'   888  888   888  888     `"Y88b.  888ooo888      888ooo888  888   888  888       888   888 888   888  888ooo888  888     
 8    Y     888  888   888  888     o.  )88b 888    .o      888    .o  888   888  888   .o8 888   888 888   888  888    .o  888     
o8o        o888o `Y8bod8P' d888b    8""888P' `Y8bod8P'      `Y8bod8P' o888o o888o `Y8bod8P' `Y8bod8P' `Y8bod88P" `Y8bod8P' d888b    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    """
      )

#AI generated Morse dictionary wiht modification on the space character.
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': f'{7*" "}'
}

#Get the input of the user
inputted_text = input("Enter a message. Your message will be converted in Morse code: ")

#Since the dictionary provides capital letters: inputted_text needs to be uppercase letters
inputted_text_uppercase = inputted_text.upper()

#Encode the text inputted from the user
encoded_message = ""
for character in inputted_text_uppercase:
    try:
        encoded_character = f"{morse_dict[character]}"
    except KeyError:
        print(f"The character {character} is not in the dictionary. This character will be ignored and not converted into Morse code.")
    else:
        #Space between words = 7 space units
        if character == " ":
            encoded_message = encoded_message.strip() #Each character has a trailing 3 space. Have to strip() in order to have 7 spaces. Otherwise, it would display 10 spaces (3+7).
            encoded_message += encoded_character
        else: #Not a space = 3 spaces between characters
            encoded_message += encoded_character + f"{3*' '}"

#Print the text in Morse code
print(f"Here's '{inputted_text}' in Morse Code: ")
print(encoded_message)


