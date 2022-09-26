"""
n1 = int(input("digite nota1"))
n2 = int(input("digite nota2"))  
n3 = int(input("digte nota3"))
n4 = int(input("digite nota4"))
n5 = int(input("digite nota5"))

N = (n1 + n2 + n3 + n4 + n5) / 5

if (n1 > N):
    print("você foi aprovado na p1")

else:

    print("vc esta reprovado na p1")


if(n2 > N):
    print("vc esta aprovado na p2")

else:
    print("vc esta reprovado na p2")

if(n3 > N):
    print("vc esta aprovado na p3")

else:
    print("vc esta reprovado na p3")

if(n4 > N):
    print("vc esta aprovado na p4")

else:
    print("vc esta reprovado na p4")

if(n5 > N):
    print("vc esta aprovado na p5")

else:
    print("vc esta reprovado na p5")
    """
    
    N = 5
    notas = []
    for i in range (1,N+1):
        x = int(input("nota:"))
        notas.append(x)


    media = 0
    for n1 in notas:
        media = media + n1
        media = media /N

    for n1 in notas:
        if n1 > media:
            print("aprovado:" , n1)

            

