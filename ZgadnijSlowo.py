import random
slowa = ("czoko","loko","oko","spoko")
word = random.choice(slowa)
poprawne = word
print(" Odgadnij Wyraz!\nMasz Tylko 5 szans!")
print("\nWyraz Sklada sie " , len(poprawne) ,"Liter!\n Wpisz Wyraz lub litere: ")
wyraz = input()
szansa = 5
while len(wyraz)>1:
	while poprawne != wyraz:
		szansa-=1
		print("pozostalo Ci ", szansa , "szans")
while len(wyraz)<2:
		print("Tak to jest")