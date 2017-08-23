import json

def main():
    while True:
        try:
            f = open("meses", encoding="utf8")
            linhas = f.readlines()
            for linha in linhas:
                print(linha.strip())
            break
        except FileNotFoundError:
            print("Tente novamente!")

if __name__ == "__main__" :
    main()
