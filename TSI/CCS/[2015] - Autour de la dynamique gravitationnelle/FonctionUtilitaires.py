#I)A)1 : ça retourne [1,2,3,4,5,6]
#I)A)2 : ça retourne [1,2,3,1,2,3]

#I.B
def smul(a,L):
    return [a*i for i in L]

#I.C.1
def vsom(L,M):
    return [L[i]+M[i] for i in range(len(L))]

#I.C.2
def vdif(L,M):
    return [L[i]-M[i] for i in range(len(L))]
