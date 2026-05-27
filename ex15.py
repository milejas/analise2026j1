valor = int(input("Digite um valor: "))

# Verifica em qual faixa o valor está
if 0 <= valor <= 10:
    print("O valor está entre 0 e 10.")
elif 11 <= valor <= 20:
    print("O valor está entre 11 e 20.")
elif 21 <= valor <= 30:
    print("O valor está entre 21 e 30.")
else:
    print("O valor está fora das faixas especificadas.")
    

