# Exercitiu 8
# Cereti user-ului sa introduca un numar intre 1 si 10. Daca nu respecta cerinta, printati un mesaj de eroare


user = int(input('Enter a number between 1 and 10:\n'))

if user in range(1, 11):
  pass
else:
  print('Error. Not within range of 1 to 10')
