"""
Exercício 1 - Conteúdos até Aula 3
Disciplina: Lógica de Programação e Algoritmos (ADS)

Programa que calcula o valor de uma compra em atacado, aplicando desconto
progressivo de acordo com faixas de valor total.
"""

print("Bem vinda Ludmila Costa!")

valor_unitario = float(input("Entre com o valor do produto: "))
quantidade = int(input("Entre com a quantidade do produto: "))
valor_total = valor_unitario * quantidade          # Calcula valor total sem desconto

if valor_total < 2500:                             # Define percentual de desconto de acordo com a faixa
    desconto = 0

elif valor_total >= 2500 and valor_total < 6000:
    desconto = 4

elif valor_total >= 6000 and valor_total < 10000:
    desconto = 7

else:                                               # Else nunca leva condição, ele significa tudo o que restou
    desconto = 11

valor_com_desconto = valor_total - (valor_total * desconto / 100)

print(f"Valor SEM desconto: R$ {valor_total:.2f}")
print(f"Valor COM desconto: R$ {valor_com_desconto:.2f}")
