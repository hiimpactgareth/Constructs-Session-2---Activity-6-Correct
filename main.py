weekend=input("Is it the weekend? ")
sunny=input("It is sunny? ")
if weekend=="yes"and sunny=="yes":
    print("We should go to the beach.")
elif weekend=="yes" and sunny=="no":
    print("We should go to the cinema.")
else:
  print("We should go to work.")
print("Have a nice day!")