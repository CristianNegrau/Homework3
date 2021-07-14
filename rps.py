# Exercitiu 7
# Jucati o tura de piatra, foarfece, hartie cu user-ul

import random

user = input('Pick rock, scissor or paper\n')
ai = random.randint(1, 3)

if user == 'rock' or user == 'scissor' or user == 'paper':
  if user == 'rock' and ai == 2:
    print('You won')
  elif user == 'scissor' and ai == 3:
    print('You won')
  elif user == 'paper' and ai == 1:
    print('You won')
  else:
    print('You lost')
else:
  print('invalid pick')
