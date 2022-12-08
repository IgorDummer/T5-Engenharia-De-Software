# explicação https://stackoverflow.com/questions/739654/how-do-i-make-function-decorators-and-chain-them-together

class NumeroUm:
    def parenteses(func):
        def wrapper(self):
            print("(", end="")
            func(self)
            print(")", end="")
        return wrapper

    def chaves(func):
        def wrapper(self):
            print("{", end="")
            func(self)
            print("}", end="")
        return wrapper

    def colchete(func):
        def wrapper(self):
            print("[", end="")
            func(self)
            print("]", end="")
        return wrapper

    @parenteses
    @chaves
    @colchete
    @colchete
    @chaves
    @parenteses
    @chaves
    @colchete
    @parenteses
    @colchete
    @chaves
    def imprimir(self):
        print('1', end="")


if __name__ == "__main__":
    teste = NumeroUm()
    teste.imprimir()
