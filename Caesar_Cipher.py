alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above


user_text = [i for i in text] #list comprehension for message
user_text

def encode(text,shift):
    new_text = []
    for i in range(0,len(text)): #loops through user message
        letter=text[i]
        if letter in alphabet: #conditional check for each letter that appears in the alphabet
            index=alphabet.index(letter) #fixed list vector names for each letter appearing in given text and alphabet
            gap=(index+shift)%26 #amount by which letter should be shifted without going out of the list range
            new_text.append(alphabet[gap])
    return new_text

if direction=='encode':
    print(''.join(encode(text,shift)))

def decode(text,shift):
    return encode((encode(text,shift)),-shift)

if direction=='decode':
    print(''.join(decode(text,shift)))


