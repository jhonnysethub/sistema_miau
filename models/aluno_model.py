def verificar_apoio(laudo, dificuldade):

    if laudo == "sim":
        return "ACOMPANHAMENTO AEE"

    elif dificuldade != "nenhuma":
        return "EM OBSERVACAO"

    else:
        return "SEM NECESSIDADE"
