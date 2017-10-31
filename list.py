"""
fichier de définition de fonctions génériques applicables sur des listes
"""



L = [1,3,4,3,5,6,3,4]



def offset(L,index) :
    half = int(len(L)/2)
    L_offset = []
    for i in range(half) :
        L_offset.append(L[i+index])
    return L_offset         #attention, renvoie une liste de longueur moitié par rapport à celle de L


def half(L) :
    half = int(len(L)/2)
    return L[0:half]


def dist(L,M) :
    assert len(L)==len(M)   #les deux listes doivent avoir la même taille n ! Cette fonction donne la somme des ecarts en valeur absolue entre L[i] et M[j]
    ecart = 0
    for i in range(len(L)) :
        ecart += abs(L[i]-M[i])
    return ecart

def scores(L) :
    liste_scores = []
    for i in range(int((len(L))/2)+1) :
        liste_scores.append(dist(half(L),offset(L,i)))
    return liste_scores

print(scores(L))
