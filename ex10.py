ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")