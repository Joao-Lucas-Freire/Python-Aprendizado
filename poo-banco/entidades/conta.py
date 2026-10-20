# Importando bibliotecas abc é uma biblioteca padrão ou nativa do python significa abstract base class  classes de bases abstratas
# serve para implementar  contratos obrigatórios que as classes filhas tem que em POO
from abc import ABC, abstractmethod

# importando da biblioteca datetime a função datetima que serve para nos entregar data e hora do momento exato da execução
from datetime import datetime

# importando uma função de um método criado nesse projeto para verificar erros
from utilitarios.exceptios import SaldoInsuficienteError

# Criando a classe conta que vai ser uma classe abstrata ou seja ela vai classe que vai servir de molde
# terá metodos que as classses filhas por obrigação teram que ter nelas também
class Conta(ABC):
    # Antes de inicializar a class adicionamos um contador para contar quantas contas tem criadas ao longo do processo
    _total_contas = 0
    def __init__(self, numero: int, cliente):  # Aqui teremos o numero da conta e os dados do cliente que já está definido na class clinte
        self._numero = numero
        self._saldo = 0.0  # Aqui definimos o atributo saldo inicia com 0 e conforme existe os depositar vai aumentando
        self._cliente = cliente  # aqui é o atributo cliente
        self._historico = []  # criamos uma lista vazia que será incrementeado com o historico fazendo assim o extrato do cliente

        Conta._total_contas += 1  # conforme adiciona contas, o contador recebe uma conta

    @property    # permite consultar o saldo e retorna o saldo como um getter
    def saldo(self):
        return self._saldo

    @classmethod   # usamos para criar um metodo para total_contas que é um atributo da classe, não do objeto
    def get_total_contas(cls):
        return cls._total_contas



    # Criando o metodo de depositar
    def depositar(self, valor: float):
        if valor > 0:   # se o valor do deposito for maior que 0
            self._saldo += valor  # saldo recebe o valor depositado
            self._historico.append((datetime.now(), f"Deposito de R$ {valor:.2f}"))
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso")

        else:
            print("Valor de depósito inválido")   # Não podemos depositar 0 ou valores negativos na conta

    # Criando metodo abstrato sacar
    @abstractmethod
    def sacar(self, valor: float):
        pass




    # Criando o metodo extrato que exibi os dados da conta
    def extrato(self):
        print(f"\n --- Extrato da conta n° {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")  # Pega o nome da classe clientes
        print(f"Saldo atual: {self._saldo:.2f}")
        print("Histórico de transações:")

        if not self._historico:  # Se não existir histórico de transação
            print("Nenhuma transação registrada.")


        for data, transacao in self._historico:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")

        print("--------------------------------------\n")

# Criando a primeira conta ou subclasse ou classe filha da classe conta
class ContaCorrente(Conta):
    def __init__(self,numero: int, cliente, limite: float = 500.00 ):
        super().__init__(numero, cliente)  # pega a inicialização para esses atributos da classe conta ou classe pai
        self.limite = limite  # atributo original e unico dessa classe

    def sacar(self, valor: float):
        if valor <= 0:
            print("Valor de saque inválido")
            return  # encerra o metdo quando o valor é invalido

        saldo_disponivel = self._saldo + self.limite

        if valor > saldo_disponivel:
            raise SaldoInsuficienteError (saldo_disponivel,valor, " Saldo e limite insuficiente")

        self._saldo -= valor
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))

        print(f"Saque de R${valor:.2f} realizado com sucesso.")

# Criando a classe ContaPoupanca que será uma filha da classe conta
class ContaPoupanca(Conta):
    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)   # Usando o super para usar a inicialização da classe pai

    def sacar(self, valor: float):
        if valor <= 0:
            print("Valor de saque inválido")
            return

        if valor > self._saldo:
            raise SaldoInsuficienteError (self._saldo, valor)

        self._saldo -= valor

        self._historico.append(
            (datetime.now(), f"Saque de R${valor:.2f}")
        )
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
















