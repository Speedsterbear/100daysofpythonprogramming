alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(mess, shift):
    encrypted_mess = []
    for i in mess:
        pos = alphabet.index(i)
        encrypted_mess.append(alphabet[pos + shift])
    print('The encoded text is ' + ''.join(encrypted_mess))
    des = input('Do you want to repeat run the code again?').lower()
    if des == 'y':
        main()
    else:
        print('Byeeeeeee :)')


def decrypt(mess, shift):
    encode_mess = []
    for i in mess:
        pos = alphabet.index(i)
        encode_mess.append(alphabet[pos - shift])
    print('The decoded text is ' + ''.join(encode_mess))
    des = input('Do you want to repeat run the code again?').lower()
    if des == 'y':
        main()
    else:
        ('Byeee! :)')


def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)

    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        print('No option selected bye :)')


main()
