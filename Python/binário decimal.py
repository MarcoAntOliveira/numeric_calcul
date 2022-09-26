
binary_number = list(input("insira o numero a ser convertido"))
binary_number[::-1]
decimal_number = 0


 for i in range (0 , len(binary_number)+1):
     decimal_number[i] = decimal_number + binary_number[i]*2**i
     


print(decimal_number)
