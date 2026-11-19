import os
from models.aluno_model import *
from utils.validacoes import *

# Caminho a partir da pasta do projeto.
# Assim funciona mesmo se o terminal estiver em outra pasta.
PASTA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO = os.path.join(PASTA, "database", "alunos.txt")


def salvar_aluno(aluno):

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:

        linha = (
            f"{aluno['nome']};"
            f"{aluno['idade']};"
            f"{aluno['turma']};"
            f"{aluno['laudo']};"
            f"{aluno['dificuldade']}\n"
        )

        arquivo.write(linha)


def gravar_todos(alunos):

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

        for aluno in alunos:

            linha = (
                f"{aluno['nome']};"
                f"{aluno['idade']};"
                f"{aluno['turma']};"
                f"{aluno['laudo']};"
                f"{aluno['dificuldade']}\n"
            )

            arquivo.write(linha)


def carregar_alunos():

    alunos = []

    try:

        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                dados = linha.strip().split(";")

                aluno = {
                    "nome": dados[0],
                    "idade": int(dados[1]),
                    "turma": dados[2],
                    "laudo": dados[3],
                    "dificuldade": dados[4]
                }

                alunos.append(aluno)

    except FileNotFoundError:
        pass

    except (IndexError, ValueError):
        print("Erro: linha com formato errado em alunos.txt.")

    return alunos


def mostrar_aluno(aluno):

    apoio = verificar_apoio(
        aluno["laudo"],
        aluno["dificuldade"]
    )

    print("\n----------------------")
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Turma:", aluno["turma"])
    print("Laudo:", aluno["laudo"])
    print("Dificuldade:", aluno["dificuldade"])
    print("Apoio:", apoio)


def listar_alunos():

    alunos = carregar_alunos()

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        mostrar_aluno(aluno)


def buscar_aluno(nome):

    alunos = carregar_alunos()

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():
            return aluno

    return None


def listar_com_laudo():

    alunos = carregar_alunos()

    for aluno in alunos:

        if aluno["laudo"] == "sim":
            print(aluno["nome"], "-", aluno["turma"])


def listar_em_observacao():

    alunos = carregar_alunos()

    for aluno in alunos:

        apoio = verificar_apoio(
            aluno["laudo"],
            aluno["dificuldade"]
        )

        if apoio == "EM OBSERVACAO":
            print(aluno["nome"], "-", aluno["turma"],
                  "-", aluno["dificuldade"])


def atualizar_aluno(nome):

    alunos = carregar_alunos()

    encontrado = False

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            aluno["turma"] = input("Nova turma: ").upper()

            laudo = input("Tem laudo? (sim/nao): ").lower()

            while validar_laudo(laudo) == False:
                print("Responda sim ou nao.")
                laudo = input("Tem laudo? (sim/nao): ").lower()

            aluno["laudo"] = laudo

            aluno["dificuldade"] = input(
                "Dificuldade (ou nenhuma): "
            ).lower()

            encontrado = True

    if not encontrado:
        print("Aluno não encontrado.")
        return

    gravar_todos(alunos)

    print("Aluno atualizado.")


def excluir_aluno(nome):

    alunos = carregar_alunos()

    novos = []

    for aluno in alunos:

        if aluno["nome"].lower() != nome.lower():
            novos.append(aluno)

    if len(novos) == len(alunos):
        print("Aluno não encontrado.")
        return

    gravar_todos(novos)

    print("Aluno excluído.")
