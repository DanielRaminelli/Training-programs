def computador_escolhe_jogada(n,m):
    if n<m:
        return n
    elif n%(m+1)>0:
        return n%(m+1)
    else:
        return m




def usuario_escolhe_jogada(c,d):
    valido=False

    while not valido:
        remv=int(input("Quantas peças você quer tirar?: "))
        if remv>d:
            print("Opa, essa jogada é inválida")
        elif remv<=0:
            print("Opa, essa jogada é inválida")
        elif remv>c:
            print("Opa, essa jogada é inválida")
        else:
            valido=True
            
    return remv

def partida():
    jogada=0
    
    valido=False
    valido2=False
    
    while not valido:
        n=int(input("Quantas peças você quer nesse jogo?"))
        if n==0:
            print("Opa, esse número não é valido, tente novamente")
        else:
            valido=True
            
    while not valido2:
        m=int(input("Qual o máximo de peças que podem ser retirardas?"))
        if m==0:
            print("Opa, esse número não é valido, tente novamente")
        else:
            valido2=True
            


    if n%(m+1)==0:
        jogada=1
        print("Você começa!")
        
        while n>0:
            if jogada==1:
                valor = usuario_escolhe_jogada(n,m)
                print("O jogador tirou",valor,"peças")
                n-=valor
                print("Restam,",n,"peças")
                jogada=2
            else:
                valor= computador_escolhe_jogada(n,m)
                print("O computador tirou",valor,"peças")
                n-=valor
                print("Restam,",n,"peças")
                jogada=1
                
        print ("Fim de jogo o computador ganhou")
        
    
    elif n%(m+1)!=0:
        jogada=2
        print("O computador começa")
        while n>0:
            if jogada==2:           
                valor = computador_escolhe_jogada(n,m)
                print("O computador tirou",valor,"peças")
                n-=valor
                print("Restam,",n,"peças")
                jogada=1
            else:
                valor = usuario_escolhe_jogada(n,m)
                print("O jogador tirou",valor,"peças")
                n-=valor
                print("Restam,",n,"peças")
                jogada=2
    print ("Fim de jogo o computador ganhou")
        
        
            
        


def campeonato():
    num=0
    while num<3:
        partida()
        num+=1
        print("Computador",num, "x 0 Você")

def main():
        print("Olá, bem vindo ao jogo do NIM")
        print("Selecione 1 se quiser jogar uma partida e selecione 2 se quiser jogar um campeonato")
        pt=int(input("Escolha: "))
        if pt>2:
            print("Essa não é uma opção válida, tente novamente")
        elif pt==1:
            print("Você escolheu partida")
            partida()
        elif pt==2:
            print("Você escolheu campeonato")
            campeonato()

main()

