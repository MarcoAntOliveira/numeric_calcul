matriz = {[1,2,3],[4,5,6],[7,8,9]}
for linha in matriz:
    for elem in linha:
        print(elem)

soma = 0
for linha in matriz:
    for elem in linha:
        soma = soma + elem

print("soma = ",soma)