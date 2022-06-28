l1=[['a','b'],['b','c','d'],['e','f']]
l2=[['p','q'],['r','s','t'],['u','v','w']]
i=0
n = [1,2,3]
while i<len(l1):
    # l1[i].extend(l2[i])
    n[i]  = l1[i]+l2[i]
    # n.append(h)
    i+=1
print(n)