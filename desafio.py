#crie um programa que o usúario digite nome, salário e valor do bonus que recebeu.
#o programa deve imprimir uma mensagem saudando o usúario pelo nome e informando o valor do salário em comparação com bônus recebido.

#calculo do KPI do bônus de 2024 é de '1000 + salário * bônus'


nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
bonus = float(input('Digite o bônus que recebeu: '))
kpi = int(1000) + salario * bonus
print(f"Olá {nome} seja bem-vindo! Seu bônus é {kpi}")