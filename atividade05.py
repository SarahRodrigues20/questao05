     print("Digite 3 números em ordem crescente e 1 aleatírio") 
num1 = int(input("Digite o seu primeiro número: "))
num2 = int(input("Digite o seu segundo número: "))
num3 = int(input("Digite o seu terceiro número: "))
num4 = int(input("Digite o seu quarto número diferente dos 3 primeiros: "))

if  num4  >  num3 :
    print ( f"A ordem decrescente dos números é: { num1 } , { num2 } , { num3 } e { num4 } " )

if  num4  >  num2  e  num3  >  num4 :
    print ( f"A ordem decrescente dos números é: { num3 } , { num4 } , { num2 } e { num1 } " )

if  num4  >  num1  e  num2  >  num4 :
    print ( f"A ordem decrescente dos números é: { num4 } , { num2 } , { num3 } e { num1 } " )

if  num4  >  num1 :
    print ( f"A ordem decrescente dos números é: { num3 } , { num2 } , { num1 } e { num4 } " )
