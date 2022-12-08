from datetime import datetime


class MensagemDoDia:
    def imprimir(self):
        print("Hoje definitivamente eh um dia")


class MensagemDomingo(MensagemDoDia):
    def imprimir(self):
        print("Hoje eh domingo.")


class MensagemSegunda(MensagemDoDia):
    def imprimir(self):
        print("Hoje eh segunda.")


class MensagemTerca(MensagemDoDia):
    def imprimir(self):
        print("Hoje eh terca.")


class MensagemQuarta(MensagemDoDia):
    def imprimir(self):
        print("Hoje eh quarta.")


class MensagemQuinta(MensagemDoDia):
    def imprimir(self):
        print("Hoje eh quinta.")


class MensagemSexta(MensagemDoDia):
    def imprimir(self):
        print("Hoje eh sexta.")


class MensagemSabado(MensagemDoDia):
    def imprimir(self):
        print("Hoje eh sabado.")


if __name__ == "__main__":

    # get current datetime
    dt = datetime.now()
    print('Datetime is:', dt)

    # get day of week as an integer
    diaSemana = dt.weekday()
    print('Day of a week is:', diaSemana)
    mensagem = MensagemDoDia()

    def switch(diaSemana):
        if diaSemana == 0:
            MensagemDomingo()
        if diaSemana == 2:
            MensagemSegunda()
        if diaSemana == 3:
            MensagemTerca()
        if diaSemana == 4:
            MensagemQuarta()
        if diaSemana == 5:
            MensagemQuinta()
        if diaSemana == 6:
            MensagemSexta()
