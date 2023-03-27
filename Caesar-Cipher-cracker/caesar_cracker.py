'''
This program can hack messages encrypted with the Caesar cipher from the previous project, 
even if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results 
to the user. In cryptography, we call this technique a brute-force attack.
'''
def Caesar(message, mode, key):
    # message: the string to be encrypted/decrypted
    # key: the encryption/decryption key
    # mode: tells the program to encrypt or decrypt
    # every possible symbol that can be encrypted
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    # stores the encrypted/decrypted form of the message
    translated = ''
    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num = LETTERS.index(symbol) # get the number of the symbol
            if mode == 'encrypt': 
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            # handle the wrap-around if num is larger than the length of LETTERS or less than 0
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol
        # print the encrypted/decrypted string to the screen  
    return translated
#######################################

message= 'This is my Secret Message.'
enc_key = 18
print('Message is: ', message)
encripted_message = Caesar(message, 'encrypt', enc_key)
print('Encripted message is: ', Caesar(message, 'encrypt', enc_key))
print('Decripted message is: ', Caesar(encripted_message, 'decrypt', enc_key))
# The program implementation brute-force attack for ciphered message
 
message = encripted_message #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# loop through every possible key
for key in range(len(LETTERS)):
    translated = ''
    # loop through each symbol in message:
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.index(symbol)
            num = num - key
            # Handle the wrap around
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            # Append the simbol without decription
            translated = translated + symbol
    print("\nDecripted message with encript key #", key, ':', translated)
    
