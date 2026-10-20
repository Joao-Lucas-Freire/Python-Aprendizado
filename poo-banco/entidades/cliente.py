class Cliente:    # Criando a classe clientes
    def __init__(self, nome: str, cpf: str ):  # definindo os atributos da classe clientes e seus tipos primitivos
        self.nome = nome
        self.cpf = cpf
        self.contas = []  # Aqui é uma lista vazia  onde adicionamos as contas do cliente


        # Criando o metodo adicionar contas para adicionar as contas do cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)  # Quando criarmos as contas do cliente será adicionado nessa lista que se inicia vazia

        # Criando o metodo str que define como vai ser a representação em string do mobjeto
    def __str__(self):
        print(f"Cliente: {self.nome} \n CPF: {self.cpf}")  # ao comando para imprimir algum objeto da classe cliente, será mostrado dessa forma














