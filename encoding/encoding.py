from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(plain_text, shift_amount, direction_amount):
  cipher_text = ""
  if shift_amount > 25:
    shift_amount = shift_amount % 25
  if direction_amount == "decode":
    shift_amount *= -1
  
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    else:
      cipher_text += char
    
  if direction_amount == "encode": 
      if new_position > len(alphabet)-1:
        new_position = new_position - len(alphabet) + 1
      print(f"The encoded text is {cipher_text}")
      


  elif direction_amount == "decode":
      if new_position < len(alphabet)+1:
        new_position = new_position + len(alphabet) - 1
      print(f"The decoded text is {cipher_text}")


  again = input("Are there any other messages you would like to encode or decode? 'yes' or 'no'\n ")
  print(again)
  if again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(plain_text, shift_amount, direction_amount)
  else:
    print("Have a great day! ")

ceaser(plain_text=text, shift_amount=shift, direction_amount=direction)

