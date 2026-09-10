"""
Exercício 2 - Conteúdos até aula 04
Disciplina: Lógica de Programação e Algoritmos (ADS)

Programa que simula o pedido de uma loja de Açaí e Cupuaçu, validando
sabor e tamanho, acumulando o valor total do pedido até o cliente
decidir encerrar.
"""

print("Bem vindo a loja de gelados da Ludmila Costa")
print("------------------" + "Cardápio" + "------------------")
print("-" * 45)

total_pedido = 0

while True:  # Laço principal - repete enquanto o cliente quiser pedir mais

    while True:  # Valida o sabor
        sabor = input("Entre com o sabor desejado (CP/AC): ").lower()
        if sabor == "cp" or sabor == "ac":
            break
        else:
            print("Sabor inválido. Tente novamente.")

    while True:  # Valida o tamanho
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").lower()
        if tamanho == "p" or tamanho == "m" or tamanho == "g":
            break
        else:
            print("Tamanho inválido. Tente novamente.")

    if sabor == "cp":  # Calcula o preço (modelo aninhado sabor + tamanho)
        if tamanho == "p":
            preco = 9
        elif tamanho == "m":
            preco = 14
        else:
            preco = 18
    else:
        if tamanho == "p":
            preco = 11
        elif tamanho == "m":
            preco = 16
        else:
            preco = 20

    if sabor == "cp":  # Converte a sigla para o nome completo, usado na exibição
        nome_sabor = "Cupuaçu"
    else:
        nome_sabor = "Açaí"

    total_pedido += preco
    print(f"Você pediu um {nome_sabor} no tamanho {tamanho.upper()}: R${preco:.2f}")

    continuar = input("Deseja pedir mais alguma coisa? (S/N): ").lower()
    if continuar == "n":
        break  # Esse break sai do laço principal
    else:
        continue

print(f"O valor total a ser pago: R${total_pedido:.2f}")
