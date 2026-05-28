print("alterado")

sexo = input("Digite o sexo (M para Masculino / F para Feminino): ")
idade = int(input("Digite a idade: "))

if sexo == "M" and idade >= 18:
    print("apto a se a listar")
else:
    print("nao apto a se alistar")
    
