"""
fichier de définition de fonctions génériques applicables sur des listes
"""



L = [1,3,4,3,5,6,-2,3,4]



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


def extract(L,fe,t) : #permet d'extraire un échantillon de durée t secondes à partir du milieu d'un morceau échantillonné à la fréquence fe
    n = len(L)
    half = int(n/2)
    E = L[half:half+int(fe*t)]
    return E

def compress(L,fe,k) :   #compresse k fois une liste de fréquence d'échantillonage fe en prélevant 1 échantillon sur k
    comp =[]
    for i in range(int(len(L)/k)) :
        comp.append(L[k*i])
    return comp,fe/k      #retourn la liste compressee et la nouvelle fréquence d'échantillonnage

def min_index(L) :
    return L.index(min(L))

def filter(L,treshold) :
    M = max(L)
    filter_L = []
    for i in L :
        if i > treshold*M :
            filter_L.append(i)
        else :
            filter_L.append(0)   #idée : si un échantillon n'est pas significatif, on le met à 0
    return filter_L

def right_tempo(tempo) :
    if tempo > 70 and tempo <140 :                  # la fin du script permet de donner un multpiple du tempo compris entre 60 et 120 bpm
        return tempo
    elif tempo < 70 :
        while tempo < 70 :
            tempo *= 2
        return tempo
    else :
        while tempo > 140 :
            tempo = tempo/2
        return tempo
