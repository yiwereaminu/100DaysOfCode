import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

def caesar(direction):
    
#encrypt function.
    def encrypt(text = text,shift=shift):

        if shift > 26:
            shift = shift % 26
        
        shifted_text = ''
        for char in text:
            if char in alphabet:
                char_ind = alphabet.index(char)
                if char_ind + shift >= len(alphabet):
                    shifted_text += alphabet[(char_ind+ shift)-len(alphabet)]
                else:
                    shifted_text +=alphabet[char_ind+shift]
            else:
                shifted_text += char
        print(f"the encrypted message is: {shifted_text}")
    
        
    def decrypt(message=text,shift=shift):
        
        if shift > 26:
            shift = shift % 26
        decrypted_message = ''
        for char in message:
           
            if char in alphabet:
                char_index = alphabet.index(char)
                decrypted_message += alphabet[char_index-shift]
            else:
                decrypted_message += char
        print(f"The decrypted message is: {decrypted_message}")
    if direction == "encode":
       encrypt(text=text, shift=shift)
    elif direction == "decode":
       decrypt(message=text, shift=shift)




while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction)
    res = input('Do you want to restart the program "Yes"|"No": ').lower()
    if res == 'no':
        should_continue = False
        print('GOOD BYE')