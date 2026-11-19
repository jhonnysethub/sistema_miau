def validar_nome(nome):

    nome = nome.replace(" ", "")

    return nome.isalpha()


def validar_idade(idade):

    return 5 <= idade <= 100


def validar_laudo(laudo):

    return laudo in ("sim", "nao")


def validar_perfil(perfil):

    return perfil in ("professor", "aee", "gestor")


def validar_email(email):

    return "@" in email and "." in email


def ler_inteiro(mensagem):

    while True:

        try:
            return int(input(mensagem))

        except ValueError:
            print("Digite apenas números.")
