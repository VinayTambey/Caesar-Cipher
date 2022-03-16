from art import logo
print(logo)

alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount):

    global direction
    caesar = ""
    if direction == "encode":
        for letter in plain_text:
            if letter in alphabet:
                letter_position = alphabet.index(letter)
                shifted_position = letter_position + shift_amount
                caesar += alphabet[shifted_position]
            else:
                caesar += letter
        print(f"The encoded text is {caesar}")

    elif direction == "decode":
        decode = ""
        for letter in plain_text:
            if letter in alphabet:
                letter_position = alphabet.index(letter)
                shifted_position = letter_position - shift_amount
                decode += alphabet[shifted_position]
            else:
                decode += letter
        print(f"The decoded text is {decode}")


should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(plain_text=text, shift_amount=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == 'no':
        print("Good Bye!")
        should_end = True
