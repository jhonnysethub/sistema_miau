from models.usuario_model import *


def exibir_menu(usuario):

    perfil = usuario["perfil"]

    print("\n===== SISTEMA MIAU =====")
    print("Usuário:", usuario["nome"], "-", perfil)

    print("\n--- ALUNOS ---")
    print("1 - Cadastrar aluno")
    print("2 - Alterar aluno")
    print("3 - Listar todos")
    print("4 - Buscar aluno")
    print("5 - Listar alunos com laudo")
    print("6 - Listar alunos em observação")

    if tem_permissao(perfil, "7"):
        print("7 - Excluir aluno")

    print("\n--- USUÁRIOS ---")
    print("8 - Cadastrar usuário")
    print("9 - Listar usuários")
    print("10 - Alterar usuário")

    if tem_permissao(perfil, "11"):
        print("11 - Excluir usuário")

    if tem_permissao(perfil, "12"):
        print("\n12 - Gerar relatório")

    print("\n0 - Sair")
