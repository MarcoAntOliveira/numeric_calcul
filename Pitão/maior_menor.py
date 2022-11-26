import numpy as np
list1 = [79.3, 75.1, 78.2, 74.1, 73.9, 75.0, 77.6, 
         77.3, 73.8, 74.6, 75.5, 74.0, 74.7, 75.9, 
          72.9, 73.8, 74.2, 78.1, 75.4, 76.3, 
         75.3, 76.2, 74.9, 78.0, 75.1, 76.8 ] 

valor_menor = 0
valor_maior = 0 


valor_media = 75.61
"""
for i in  list1:
    if i > valor_media:
        np.insert(list2 , valor_maior - 1, i)
        valor_maior += 1
        
        
        
for i in list1:                
    if i < valor_media:
        np.insert(list3 , valor_menor - 1, i)
        valor_menor += 1
   """
list1.sort()
print(list1) 
list2 =[i for i in list1[0:16]]
print("list2", list2)

list3 =[i for i in list1[17:27]] 
print("list3", list3)
        
for i in  list1:
    if i > valor_media:
        print("valor maior" , valor_maior, i)   
        valor_maior += 1
        
"""        
print("\n\n\n")       
        
for i in  list1: 
    if i < valor_media:
        print("valor menor", valor_menor, i)
        valor_menor += 1
"""


print(valor_menor, valor_maior, list2, list3)       
              
