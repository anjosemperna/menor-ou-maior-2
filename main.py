import random
pontos_seus = 0
pontos_deles = 0
while(True):
  cor_secreta = random.choice(['R','G','B'])
  palpite = input("Adivinhe a cor (R,G,B): ").upper()
  if palpite not in ['R','G','B']:
    print("Entrada invalida. Escolha o R, G ou B.")
  elif palpite == cor_secreta:
    print("Parabens! Você acertou!")
    pontos_seus = pontos_seus +1
  else:
    print('Opss, VOCÊ ERROU HAHAHA')
    pontos_deles = pontos_deles +1
  print('A cor era', cor_secreta)
  print(f'VOCÊ {pontos_seus} X PC {pontos_deles}')