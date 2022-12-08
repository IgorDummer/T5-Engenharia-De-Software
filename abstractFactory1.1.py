import random


class HelloWorld:

    def __init__(self, print_factory=None):

        self.print_factory = print_factory

    def show_print(self):
        """Cria e printa o HelloWorld usando abstract factory"""

        helloWorld = self.print_factory()
        helloWorld.printHelloWorld()


class helloWorldPrompt:

    """Classe para imprimir no terminal"""

    def printHelloWorld(self):
        return print("Hello, World!")


class helloWorldTxt:

    """Classe para imprimir no arquivo output.txt"""

    def printHelloWorld(self):
        with open('output.txt', 'w') as f:
            f.write("Hello, World!")


def randomHelloWorld():
    """Randomiza a escolha"""

    return random.choice([helloWorldPrompt, helloWorldTxt])()


if __name__ == "__main__":

    helloWorld = HelloWorld(randomHelloWorld)
    helloWorld.show_print()
