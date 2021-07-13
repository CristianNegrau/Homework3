# Exercitiu 3
list = ["a", "b", "c", "a", "d", "e", "b", "a"]
# Creati o noua lista care sa fie ca cea de mai sus dar fara litera a

for i in list:
  if 'a' in list:
    list.remove('a')

print(list)
