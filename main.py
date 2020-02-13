ask = input("Are you encrypting or decrypting? Enter 'e' or 'd'")

string = input("Enter message!")
alphabet = "abcdefghijklmnopqrstuvwxyz"
newstring = ""

key = int(input("Enter Key"))


i = 0
while i < len(string):
  letter = string[i]
  whereisletter = alphabet.find(letter)
  if ask == 'e':
    newletter = alphabet[(whereisletter + key)%26]
  else:
    newletter = alphabet[(whereisletter - key)%26]
  newstring = newstring+newletter
  i+=1
print newstring

