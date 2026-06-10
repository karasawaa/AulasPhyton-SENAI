num1 = 0
num2 = 0
result = 0
acao = 0
i = 0
continuar = ""

print("------Calculadora------")
while (True) :

    if (acao == 1) :    #Adição
        result = num1 + num2
        print(f"\nResultado: {result}")
        
        while (continuar != "y") :

            continuar = str(input("Deseja continuar? (Y/N): "))

            if (continuar == "n") :
                break 
            elif (continuar == "y") :
                i = i + 1
                break
            else : 
                print("\nDigite uma opção válida IMBECIL")

    elif (acao == 2) :  #Subtração
        result = num1 - num2
        print(f"\nResultado: {result}")

        while (continuar != "y") :
            continuar = str(input("Deseja continuar? (Y/N): "))

            if (continuar == "n") :
                break 
            elif (continuar == "y") :
                i = i + 1
                break
            else : 
                print("\nDigite uma opção válida IMBECIL")

    elif (acao == 3) :  #Multiplicação
        result = num1 * num2
        print(f"\nResultado: {result}")

        while (continuar != "y") :
            continuar = str(input("Deseja continuar? (Y/N): "))

            if (continuar == "n") :
                break 
            elif (continuar == "y") :
                i = i + 1
                break
            else : 
                print("\nDigite uma opção válida IMBECIL") 

    elif (acao == 4) :  #Divisão
        if (num2 == 0) :
                print("Não divide por 0 ANIMAL")
        else :
            result = num1 / num2
            print(f"\nResultado: {result}")

        while (continuar != "y") :
            continuar = str(input("Deseja continuar? (Y/N): "))

            if (continuar == "n") :
                break 
            elif (continuar == "y") :
                i = i + 1
                break
            else : 
                print("\nDigite uma opção válida IMBECIL")

    elif (acao == 5) :  #Sair
        break
    else :
        print("\nDigite um número correto")

    if (continuar == "n") :
        break

    continuar = ""
    acao = int(input("""
1- Adição
2- Subtração
3- Multiplicação
4- Divisão
5- Sair

Selecione sua opção: """))

    if (i == 0) :  
            num1 = int(input("1º Número: "))
            num2 = int(input("2º Número: "))
    else :  
        num1 = result
        print (f"1º Número: {num1}")
        num2 = int(input("2º Número: "))
    
