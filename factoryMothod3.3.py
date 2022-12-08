import sys
import random


class ArquivoLog:
    def exibeLog():
        with open('log.txt', 'w') as f:
            for i in range(10):
                f.write(str(i+1) + '\n')


class ConsoleLog:
    def exibeLog():
        for i in range(10):
            print(i+1)


def Factory(log):
    """Factory Method"""
    types = {
        "arquivo": ArquivoLog,
        "console": ConsoleLog,
    }
    return types[log]


def retornaArgumento():
    types = ['arquivo', 'console']
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return str(random.choice(types))


if __name__ == "__main__":
    log = Factory(retornaArgumento())
    log.exibeLog()
