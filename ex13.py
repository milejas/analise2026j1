idade = int(input("Digite a idade: "))
if idade < 0:
    print("Idade inválida! Por favor, digite um número positivo.")
elif idade < 18:
    print("É menor de idade.")
elif idade < 60:
    print("É maior de idade (adulto).")
else:
    print("É idoso.")