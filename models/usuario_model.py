# Opções do menu que cada perfil pode usar.
# 7 e 11 = excluir | 12 = relatório

PERMISSOES = {
    "professor": ("1", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "11"),

    "aee": ("1", "2", "3", "4", "5", "6",
            "8", "9", "10"),

    "gestor": ("1", "2", "3", "4", "5", "6", "7",
               "8", "9", "10", "11", "12")
}


def tem_permissao(perfil, opcao):

    return opcao in PERMISSOES[perfil]
