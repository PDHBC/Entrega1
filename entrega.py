lista_onibus = []
dic_pontos = {}
lista_motoristas =[]
lista_fiscais = []
class Onibus:
    def __init__(self, codigo, motorista=None, fiscal=None, rota=[]):
        self.codigo = codigo
        self.motorista = motorista
        self.fiscal = fiscal
        self.rota = rota

    def __str__(self):
        return  f"Codigo : {self.codigo} \
                \n  Motorista : {'Não tem Motorista' if self.motorista == None else self.motorista} \
                \n  Fiscal : {'Não tem Fiscal' if self.fiscal == None else self.fiscal} \
                "

    def __repr__(self) :
        return  f"Codigo : {self.codigo} \
                \n  Motorista : {'Não tem Motorista' if self.motorista == None else self.motorista} \
                \n  Fiscal : {'Não tem Fiscal' if self.fiscal == None else self.fiscal} \
                "
        
class Ponto:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
    def __str__(self) :
        return f" Ponto de Parada : {self.codigo}"
    def __repr__(self) :
        return f" Ponto de Parada : {self.codigo}" 

class Fiscal:
    def __init__(self, nome, onibus):
        self.nome = nome
        self.onibus = onibus
    def __repr__(self):
        return f"Fiscal : {self.nome}"
    def __str__(self):
        return f"Fiscal : {self.nome}"
        

class Motorista:
    def __init__(self, nome, onibus):
        self.nome = nome
        self.onibus = onibus
    def __repr__(self):
        return f"Fiscal : {self.nome}"
    def __str__(self):
        return f"Fiscal : {self.nome}"

def criar_onibus(codigo, motorista='Não tem Motorista', fiscal='Não tem Fiscal', rota=[]):
    """"
    vou usar as classes onibus,motorista e fiscal da seguinte maneira:
    quando criar eles vou adiciona-los a listas para facilitar a função
    mostrar onibus/motoristas/fiscais
    """

    onibus = Onibus(codigo,motorista,fiscal,rota)
    lista_onibus.append(onibus)

def criar_motorista(nome, onibus='Não está em um onibus'):
    motorista = Motorista(nome, onibus)
    lista_motoristas.append(motorista)

def criar_fiscal(nome, onibus='Não está em um onibus'):
    fiscal = Fiscal(nome, onibus)
    lista_fiscais.append(fiscal)

def criar_ponto(codigo, nome): 
    """""
    vou usar os pontos de parada da seguinte maneira :
    quando criar eles vou adicionar eles em um dicionário (dic_pontos)
    no qual os valores vão ser os nomes e as chaves vão ser
    os códigos, isso para facilitar o armazenamento deles e 
    a adição deles nas rotas dos onibus
    """
    ponto = Ponto(codigo, nome)  
    dic_pontos[ponto.codigo] = ponto.nome

def mostrar_onibus():
    print("Codigo   Motorista        Fiscal")
    for onibus in lista_onibus:
        print(f"{onibus.codigo:<8} {onibus.motorista:<16} {onibus.fiscal:<16}")

def mostrar_motoristas():
    print("Motorista       Onibus")
    for motorista in lista_motoristas:
        print(f"{motorista.nome:<16} {motorista.onibus:<8}")

def mostrar_fiscais():
    print("Fiscal          Onibus")
    for fiscal in lista_fiscais:
        print(f"{fiscal.nome:<16} {fiscal.onibus:<8}")

def deletar_onibus(codigo_do_onibus):
    for onibus in lista_onibus:
        if onibus.codigo == codigo_do_onibus:
            lista_onibus.remove(onibus)
            break

def deletar_fiscal(nome_do_fiscal):
    for fiscal in lista_fiscais:
        if fiscal.nome == nome_do_fiscal:
            lista_fiscais.remove(fiscal)
            break

def deletar_motorista(nome_do_motorista):
    for motorista in lista_motoristas:
        if motorista.nome == nome_do_motorista:
            lista_motoristas.remove(motorista)
            break

def deletar_ponto(codigo_do_ponto):
    del(dic_pontos)[codigo_do_ponto]
    for onibus in lista_onibus:
        if codigo_do_ponto in onibus.rota:
            onibus.rota.remove(codigo_do_ponto)
            break

def assignar_motorista(nome_do_motorista, codigo_do_onibus):
    for motorista in lista_motoristas:
        if motorista.nome == nome_do_motorista:
            motorista.onibus = codigo_do_onibus
    for onibus in lista_onibus:
        if onibus.codigo == codigo_do_onibus:
            onibus.motorista = nome_do_motorista

def assignar_fiscal(nome_do_fiscal, codigo_do_onibus):
    for onibus in lista_onibus:
        if onibus.codigo == codigo_do_onibus:
            onibus.fiscal = nome_do_fiscal
    for fiscal in lista_fiscais:
        if fiscal.nome == nome_do_fiscal:    
            fiscal.onibus = codigo_do_onibus
    
def adicionar_ponto_de_parada(nome_do_ponto, codigo_do_onibus):
    for onibus in lista_onibus:
        if onibus.codigo == codigo_do_onibus:
            if nome_do_ponto not in onibus.rota:
                onibus.rota += [nome_do_ponto]


