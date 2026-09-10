"""
Exercício 3 - Conteúdos até aula 05
Disciplina: Lógica de Programação e Algoritmos (ADS)

Sistema de cobrança de uma copiadora, com funções para escolher o
serviço, informar o número de páginas (com desconto progressivo) e
escolher um adicional de encadernação.
"""

print("Bem vindo a Copiadora da Ludmila Costa")


def escolha_servico():
    """Pergunta o serviço desejado e retorna a sigla válida (dig/ico/ipb/fot)."""
    while True:
        print("Entre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico = input().lower()

        if servico in ["dig", "ico", "ipb", "fot"]:
            return servico
        else:
            print("Escolha inválida, entre com o tipo do serviço novamente")


def num_pagina():
    """Pergunta o número de páginas e retorna o valor já com desconto aplicado."""
    while True:
        print('Entre com o número de páginas desejado')
        try:
            paginas = int(input())
            if paginas >= 20000:
                print("Não aceitamos tantas páginas de uma vez")
                print("Entre com o número de páginas novamente")
                continue
            else:
                if paginas < 20:
                    desconto = 0
                elif paginas >= 20 and paginas < 200:
                    desconto = 15
                elif paginas >= 200 and paginas < 2000:
                    desconto = 20
                else:
                    desconto = 25

                paginas_com_desconto = paginas - (paginas * desconto / 100)
                return paginas_com_desconto
        except:
            continue


def servico_extra():
    """Pergunta pelo adicional de encadernação e retorna o valor extra em reais."""
    while True:
        print('Deseja adicionar algum serviço?')
        print("1 - Encadernação Simples - R$15.00")
        print("2 - Encadernação Capa Dura - R$40.00")
        print("0 - Não desejo mais nada")
        servico_extra = int(input())
        if servico_extra == 1:
            return 15
        elif servico_extra == 2:
            return 40
        elif servico_extra == 0:
            return 0
        else:
            print('Deseja adicionar algum serviço?')


sigla = escolha_servico()  # retorna "dig", "ico", "ipb" ou "fot"

if sigla == "dig":
    preco_servico = 1.10
elif sigla == "ico":
    preco_servico = 1.00
elif sigla == "ipb":
    preco_servico = 0.40
else:
    preco_servico = 0.20

paginas = num_pagina()
extra = servico_extra()

total = (preco_servico * paginas) + extra

print(f"Total: R${total:.2f} (serviço: {preco_servico} * páginas: {paginas} + extra: {extra:.2f})")
