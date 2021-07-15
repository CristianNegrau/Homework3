# Exercitiu 11
# Intrebati-l pe user parola si ziceti daca e slaba, moderata sau puternica. Daca e sub 10 caractere e slaba, iar peste 20 puternica

user = input('Enter a password:\n')

while len(user) > 0:
  if len(user) < 10:
    print('Weak password')
  elif len(user) <= 20 and len(user) >= 10:
    print('Moderate password')
  else:
    print('Strong password')
  break
