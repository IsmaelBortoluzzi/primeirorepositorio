from read_int_float import leiaint
usuarios = {}
user_id = 100


class Usuario:
    # Biblioteca para usar criptografias
    from passlib.hash import pbkdf2_sha256 as sha256  # pip install passlib

    def __init__(self, nome, cpf, senha, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = Usuario.sha256.hash(senha, rounds=3000, salt_size=16)  # encripta a senha
        self.__email = email
        self.carrinho = []
        self.limite = 1000

    def checa_cpf(self):
        return self.__cpf

    def mostra_nome(self):
        return self.__nome

    def checa_senha(self, senha_func):
        if Usuario.sha256.verify(senha_func, self.__senha):  # verifica a senha
            return True
        return False

    def mostra_email(self):
        return self.__email


def make_users(nome, cpf, senha, email):
    user = Usuario(nome, cpf, senha, email)
    return user


def cadastro():
    global user_id
    global usuarios
    name = str(input("Digite o seu nome: "))
    cpf = leiaint("Digite o cpf: ")

#    while not teste_cpf(cpf):
#        print("CPF inválido!")
#        cpf = leiaint("Digite o cpf: ")

    for k in usuarios.keys():
        if usuarios[k].checa_cpf() == cpf:
            print(f"Este usuário já existe!")
            return None

    email = str(input("Digite o seu e-mail: "))
    senha = str(input("Digite uma senha"))
    verify_senha = input("Digite novamente a senha: ")

    while senha != verify_senha:
        print("Senha incorreta!")
        senha = str(input("Digite uma senha"))
        verify_senha = input("Digite novamente a senha: ")

    usuarios["user_id_" + str(user_id)] = make_users(name, cpf, senha, email)
    user_id += 1
    return None


def saldo(user_id2):
    return usuarios["user_id_" + str(user_id2)].limite


def comprar(senha, userid1):
    if not usuarios["user_id_" + str(userid1)].checa_senha(senha):
        print("Senha incorreta!")
        return None

    while True:
        for i in lista_de_produtos:
            print(f"{i[0], i[1]}")

        pro = leiaint("Qual produto deseja comprar? (insira o id do produto ou 0 para sair): ")

        if 1 > pro > 20:
            return None

        if usuarios["user_id_" + userid1].limite - lista_de_produtos[pro][1] <= 0:
            print(f"O Carrinho está cheio. Pague para poder comprar mais!")
            return None

        usuarios["user_id_" + userid1].carrinho.append(lista_de_produtos[pro])
        usuarios["user_id_" + userid1].limite -= lista_de_produtos[pro][1]


lista_de_produtos = ('', ["1. arroz 5kg", 10.99], ["2. feijão 1kg", 7.99])

cadastro()
cadastro()

for i, v in usuarios.items():
    print(i, v.mostra_nome())

print(usuarios["user_id_0"].mostra_nome())
