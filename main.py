from alphabet import alphabet
from art import logo
print(logo)

flag=True

def ceaser(text,shift,direction):
  if(shift>26):
    shift=shift%26
  if direction=='decode':
    shift*=-1
  final=[]
  for x in text:
    if x not in alphabet:
      final.append(x)
      continue
    new=alphabet.index(x)
    new=new+shift
    final.append(alphabet[new])

  print(f"original message is {text}")
  print(f"{direction}d message is {''.join(final)}")


def Interface():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceaser(text,shift,direction)

  
while(flag==True):
  Interface()
  choice=input("Do you wish to exit the cypher process?")
  if(choice=='yes'):
    flag=False
    print('Goodbye')
    
