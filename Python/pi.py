import matplotlib.pyplot as plt
lottery = [3, 42, 12, 19, 30, 59]

lottery. sort()
print(lottery)

lottery.reverse()
print(lottery)

lottery.append(190)
print(lottery)

print(lottery[0])

lottery.pop(0)
print(lottery)

participant ={'name':'ola', 'country':'poland', 'favorite_numbers' : [7, 42, 92]}

print(participant['country'])

print(len(participant))
participant['favorite_language'] = 'python'

print(len(participant))
w = [ 159, 164.4, 164.9, 165, 165.8, 166.9, 167.3, 168.5,
     169, 169.8, 170.3, 170.4, 170.8, 171, 171.1, 172,
     172.1, 173.3, 173.9, 174.1, 174.3, 174.4, 174.6,
     174.7, 175.1, 175.5, 175.6, 176.1, 176.4, 176,8,
     177.4, 177.8, 177.9, 178.7, 179, 179.9, 180.8,
     180.8, 181.5, 185.5 ]
plt.hist(w)
plt.show(hist(w b ))