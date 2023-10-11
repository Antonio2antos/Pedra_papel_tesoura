import random

jogador1 = input("Jogador 1, escolha: pedra, papel ou tesoura: ")
jogador2 = random.choice(["pedra", "papel", "tesoura"])

if jogador1.lower() == jogador2:
    print("Empate!")
elif jogador1.lower() == "pedra" and jogador2 == "tesoura":
    print("Jogador 1 ganha! (Pedra ganha a tesoura!)")
elif jogador1.lower() == "papel" and jogador2 == "pedra":
    print("Jogador 1 ganha! (Papel ganha a pedra!)")
elif jogador1.lower() == "tesoura" and jogador2 == "papel":
    print("Jogador 1 ganha! (Tesoura ganha a papel!)")
else:
    print("Jogador 2 ganha!")
