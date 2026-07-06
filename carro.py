class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.estado = "parado" #parado, movendo, freiando
        self.ligado = False
        self.velocidade = 0

    def acelerar(self):
        if (self.ligado == True and self.estado != "freiando"):
            self.estado = "movendo"
            print(f'\n{self.estado}')
            self.velocidade += 10
            print(f'Velocidade = {self.velocidade}km/h')
        else:
            print('\nNAO E POSSIVEL')

    def freiar(self):
        if (self.ligado == True and self.estado == "movendo"):
            self.estado = "freiando"
            print(f'\n{self.estado}')
            self.velocidade -= 10
            print(f'Velocidade = {self.velocidade}km/h')
            if (self.velocidade > 0):
                self.estado = "movendo"
            else:
                self.estado = "parado"
        else:
            print('\nNAO E POSSIVEL')
    
    def ligar(self):
        if (self.ligado == True):
            print('\nCARRO JA ESTA LIGADO')
        else:
            print('\nLIGANDO... \nLIGADO')
            self.ligado = True

    def desligar(self):
        if (self.ligado == False):
            print('\nCARRO JA ESTA DESLIGADO')
        elif (self.ligado == True and self.velocidade > 0):
            print('\nCARRO EM MOVIMENTO')            
        elif (self.ligado == True and self.velocidade == 0):
            print('\nDESLIGANDO')
            self.ligado = False

carro1 = Carro('CELTA')

print(f"<<------ Carro: {carro1.nome}------>>")
while True:
    print("\n1-Acelerar \n2-Freiar \n3-Ligar \n4-Desligar")
    escolha = input("\nSelecione o que deseja fazer: ")

    if escolha in ["1", "2", "3", "4"]:
        if escolha == "1" :
            carro1.acelerar()
        elif escolha == "2" :
            carro1.freiar()
        elif escolha == "3" :
            carro1.ligar()
        elif escolha == "4" :
            carro1.desligar()
    else:
        print('\nESCOLHA DIREITO')
