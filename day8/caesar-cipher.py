alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text_array = list(text)


def ceaser_cipher():
    cipher_array = []
    for i in range(0, shift):
        index = alphabet.index(text_array[i])
        if direction == 'encode':
            x = alphabet[index + shift]
        else:
            x = alphabet[26 + index - shift]
        cipher_array.append(x)

    print(f"{' '.join(cipher_array)}")


ceaser_cipher()
