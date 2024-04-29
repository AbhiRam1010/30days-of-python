alphabet = 'a b c d e f g h i j k l m n o  p q r s t u v w x y z a b c d e f g h i j k l m n o  p q r s t u v w x y z'.split()
direction=input(f'Enter the direction you want to shift "Encode" or "Decode":  ').lower()
text = input("Type your messege: \n").lower()
shift = int(input("Enter the number of shift you want: \n"))
shift = shift%26

def encrypt(box_text,shift_amount,direction):
        cipher_text= ""
        for n in box_text:
            if direction== "encode":
                shift_amount=shift_amount
            elif direction== "decode":    
                shift= -1*shift
            position= alphabet.index(n)
            new_position= position+shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
            # elif direction=='decode':
            #     position= alphabet.index(n)
            #     new_position= position-shift_amount
            #     new_letter = alphabet[new_position]
            #     cipher_text += new_letter
        print(f'The {direction}d text is {cipher_text}')
        

encrypt(box_text=text,shift_amount=shift,direction=direction)

