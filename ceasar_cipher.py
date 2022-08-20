alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(cipher_text,cipher_shift,cipher_direction):
    result = ""
    if cipher_direction == 'decode':
            cipher_shift *= -1
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position + cipher_shift
        new_letter = alphabet[new_position]
        result += new_letter
    print(f"Your {direction}d text is {result}")
                
            
        
caesar(cipher_text=text, cipher_shift=shift, cipher_direction=direction)
        


    