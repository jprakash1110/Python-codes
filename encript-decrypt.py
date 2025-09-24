
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',

            'u', 'v', 'w', 'x', 'y', 'z']

 

def chyper(original_tetx, shift_amount, encode_or_decode):

    output_text = ""

   

    if encode_or_decode == "decode":

                shift_amount = -shift_amount

 

    for letter in original_tetx:

 

        if letter  not in alphabet:

            output_text += letter 

 

        else:

           

            shift_number = (alphabet.index(letter)) + shift_amount

            shift_number %= len(alphabet)

            output_text += alphabet[shift_number]

    print(f"your {encode_or_decode}d result is: {output_text}")

 

restart = True

 

while restart:

     

    direction = input("Enter encode to encrypt and decode to decrypt \n").lower()

    text = input("Enter the word which you want to encrypt or decrypt \n").lower()

    shift = int(input("Enter the number by which you want to shift the letters to encrypt or decrypt \n"))

 

    chyper(original_tetx=text, shift_amount=shift, encode_or_decode=direction)

 

    choice = input("Press yes if you want to run it again and no to quit execution \n")

    if choice == "no":

         restart = False

         print("GoodBye")