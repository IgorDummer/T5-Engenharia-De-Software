from abc import ABC, abstractmethod
import random


class Strategy(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass


class Context:
    strategy: Strategy  # the strategy interface

    def setStrategy(self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Default()

    def executeStrategy(self) -> str:
        print(f'Hoje é {self.strategy.execute()}.')


class StrategyDomingo(Strategy):
    def execute(self) -> str:
        return "Domingo"


class StrategySegunda(Strategy):
    def execute(self) -> str:
        return "Segunda"


class StrategyTerca(Strategy):
    def execute(self) -> str:
        return "Terça"


class StrategyQuarta(Strategy):
    def execute(self) -> str:
        return "Quarta"


class StrategyQuinta(Strategy):
    def execute(self) -> str:
        return "Quinta"


class StrategySexta(Strategy):
    def execute(self) -> str:
        return "Sexta"


class StrategySabado(Strategy):
    def execute(self) -> str:
        return "Sábado"


class Default(Strategy):
    def execute(self) -> str:
        return "um dia"


def diaAleatorio(self):
    dias = ['domingo', 'segunda', 'terça',
            'quarta', 'quinta', 'sexta', 'sabado']
    aleatorio = random.choice(dias)
    types = {
        "domingo": StrategyDomingo,
        "segunda": StrategySegunda,
        "terça": StrategyTerca,
        "quarta": StrategyQuarta,
        "quinta": StrategyQuinta,
        "sexta": StrategySexta,
        "sabado": StrategySabado
    }
    return types[aleatorio]


    # Example application
app = Context()
app.setStrategy(diaAleatorio())
app.executeStrategy()
