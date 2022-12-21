# Link: https://colab.research.google.com/drive/1pjlJYJzCCRGoQVKadv0HMfWjCCs0IHmp?usp=sharing

class NomeSobrenome:
    def exibeNome(nome):
        print(nome)


class SobrenomeNome:
    def exibeNome(nome):
        for i in range(len(nome)):
            if nome[i] == ",":
              separacao = i
        i = separacao
        print(nome[i+2:], nome[0:i])


def Factory(tipo):
    localizers = {
        "A": NomeSobrenome,
        "B": SobrenomeNome
    }
    return localizers[tipo]


def tipo(nome):
    aux = 0
    for i in range(len(nome)):
        if nome[i] == ",":
            aux = 1
    if aux == 1:  
        return "B"
    else:
        return "A"

 
if __name__ == "__main__":
        
    nomes = ["Nate Macauly", "Jackson, Percy", "Lynch, Ronan"]

    for i in nomes:
      Factory(tipo(i)).exibeNome(i)
