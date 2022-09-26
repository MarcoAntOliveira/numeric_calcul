

conv = list(range(0,12))

for i in range(0, 10):
    conv[i] = 0
    
conv[11] = 0
conv[10] = "."
    
print(conv)

num_frac = float(input("numero a ser convertido"))
print("%.3f" % num_frac)
    for i in range(0, 10):
        num_frac = 2*num_frac
        if(num_frac > 1):
             conv[i] = 1
             num_frac = num_frac - 1
        elif(num_frac < 1):
            conv[i] = 0
        elif(num_frac == 1)
            conv[i] = 1
            
print (conv)
        



"""
//remove colchetes e virgulas
conv = input().split
conv = [int(x) for x in conv]
maior_numero = max(conv)

for i in range (len(conv)):
    conv[i] = maior_numero - conv[i]
    
print (conv)

"""