emocao = input("Digite uma emoção: ")

match emocao.upper():
    case "FELIZ":
        print(":)")
    case "TRISTE":
        print(":(")
    case "NERVOSO":
        print("X(")
    case "INDIFERENTE":
        print(":|")
    case _:
        print("Emoção Inválida.")