def contagemRegressiva(contagem: int) -> None:
    if (contagem < 0):
        print("Contagem Regressiva finalizada!")
        return
    print(f"{contagem}", end='')

    if(contagem != 0):
        print(",", end=' ')
    else:
        print(".")

    contagemRegressiva(contagem - 1)

contagemRegressiva(5)