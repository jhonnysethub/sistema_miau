from controllers.aluno_controller import *
from controllers.usuario_controller import *
from views.menu_view import *

print("===== LOGIN MIAU =====")
print("Logins de teste (senha 1234):")
print("  gestor@miau.com   -> gestor")
print("  carlos@miau.com   -> professor")
print("  ana@miau.com      -> aee")

usuario_logado = None

while usuario_logado is None:

    email = input("E-mail: ")
    senha = input("Senha: ")

    usuario_logado = fazer_login(email, senha)

    if usuario_logado is None:
        print("E-mail ou senha incorretos.")

print("Bem-vindo(a),", usuario_logado["nome"])

while True:

    exibir_menu(usuario_logado)

    opcao = input("Escolha uma opção: ")

    if opcao != "0" and not tem_permissao(usuario_logado["perfil"], opcao):
        print("Acesso negado ou opção inválida.")
        continue

    if opcao == "1":

        nome = input("Nome: ")

        while validar_nome(nome) == False:
            print("Nome inválido.")
            nome = input("Nome: ")

        idade = ler_inteiro("Idade: ")

        while validar_idade(idade) == False:
            print("Idade inválida.")
            idade = ler_inteiro("Idade: ")

        turma = input("Turma: ").upper()

        laudo = input("Tem laudo? (sim/nao): ").lower()

        while validar_laudo(laudo) == False:
            print("Responda sim ou nao.")
            laudo = input("Tem laudo? (sim/nao): ").lower()

        dificuldade = input(
            "Dificuldade (ex.: atencao, leitura ou nenhuma): "
        ).lower()

        aluno = {
            "nome": nome,
            "idade": idade,
            "turma": turma,
            "laudo": laudo,
            "dificuldade": dificuldade
        }

        salvar_aluno(aluno)

        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":

        nome = input("Nome do aluno para alterar: ")

        atualizar_aluno(nome)

    elif opcao == "3":

        listar_alunos()

    elif opcao == "4":

        nome = input("Nome do aluno: ")

        aluno = buscar_aluno(nome)

        if aluno:
            mostrar_aluno(aluno)

        else:
            print("Aluno não encontrado.")

    elif opcao == "5":

        print("\n=== ALUNOS COM LAUDO ===")
        listar_com_laudo()

    elif opcao == "6":

        print("\n=== ALUNOS EM OBSERVAÇÃO ===")
        listar_em_observacao()

    elif opcao == "7":

        nome = input("Nome do aluno para excluir: ")

        excluir_aluno(nome)

    elif opcao == "8":

        nome = input("Nome: ")

        while validar_nome(nome) == False:
            print("Nome inválido.")
            nome = input("Nome: ")

        email = input("E-mail: ")

        while validar_email(email) == False:
            print("E-mail inválido.")
            email = input("E-mail: ")

        senha = input("Senha: ")

        perfil = input("Perfil (professor/aee/gestor): ").lower()

        while validar_perfil(perfil) == False:
            print("Perfil inválido.")
            perfil = input("Perfil (professor/aee/gestor): ").lower()

        usuario = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "perfil": perfil
        }

        salvar_usuario(usuario)

        print("Usuário cadastrado com sucesso!")

    elif opcao == "9":

        listar_usuarios()

    elif opcao == "10":

        email = input("E-mail do usuário para alterar: ")

        atualizar_usuario(email)

    elif opcao == "11":

        email = input("E-mail do usuário para excluir: ")

        excluir_usuario(email)

    elif opcao == "12":

        gerar_relatorio()

    elif opcao == "0":

        print("Sistema encerrado.")
        break
