# menu principal


def leiaint(i=''):
    """
    É uma função idêntica ao input() porém trata a entrada
    para aceitar somente int

    :param i: É a string que apare pro usuário antes do input
    :return: um número int
    """
    while True:
        try:
            entrada = int(input(i))
        except KeyboardInterrupt:
            print('O usuário preferiu não informar o valor')
            return 0
        except:
            print('Você não digitou um número inteiro!')
            continue
        else:
            return entrada


def titulo(t):
    """
    :param t: Título a ser escrito
    :return: Título formatado bonito
    """
    print('-'*len(t))
    print(f'{t}')
    print('-'*len(t))


opcao = -1

while opcao != 0:
    titulo('MENU PRINCIPAL')
    print("""
1 - Cadastro
2 - Comprar
3 - Mostrar carrinho
4 - Pagar conta
5 - Consultar cliente
6 - Mostrar produtos
0 - Sair""")
    opcao = leiaint("\nOpção: ")

'''

    if opcao == 1:
        print("Opção selecionada: Cadastro")
        index = cadastro()

    elif opcao == 2:
        print("Opção selecionada: Comprar")
        cpf = input("Digite  o cpf: ")
        senha = input("Digite  a senha: ")
        comprar(cpf, senha)

    elif opcao == 3:
        print("Opção selecionada: Mostrar carrinho")

    elif opcao == 4:
        print("Opção selecionada: Pagar conta")

    elif opcao == 5:
        print("Opção selecionada: Consultar cliente")
        consulta_cliente()

    elif opcao == 6:
        print("Opção selecionada: Mostrar produtos na prateleira")
        mostra_produtos()

    elif opcao == 0:
        print("Saindo...")

    else:
        print("Opção inválida! Tente novamente.")
'''
