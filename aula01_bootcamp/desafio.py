

Constante_bonus = 1000

#1) Solicita ao usuário que digite seu nome 
nome =input("Digite seu nome:")

#2) Solicita ao usuário que digite o valor do seu salário
salario = float(input("Digite o valor do seu salário mensal:"))
#Converte a entrada para um número de ponto flutuante
#3) Solicita ao usuário que digite o valor do bônus recebic
bonus = float(input("Digite o valor do bônus recebido:"))
#Converte a entrada para um número de ponto flutuante
#4) Calcule o valor do bônus final
valor = Constante_bonus  + salario + bonus
#5) Imprima a mensagem personalizada incluindo o nome do usuário, salário  e o valor do bônus final
print(f"O usuário {nome} possui o bonus de {valor}")