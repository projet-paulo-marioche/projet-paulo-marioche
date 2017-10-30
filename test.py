import math
import numpy as np
from matplotlib.pyplot import *
import scipy.io.wavfile as wave
from numpy.fft import fft

"""
Ouverture du fichier .wav, représentation temporelle
"""

rate,data = wave.read('loop_batterie.wav')   #rate = frequence d'échantillonage, déjà intégrée dans le fichier .wav
n = len(data)                #nombre d'échantillons
duree = 1.0*n/rate



te = 1.0/rate
t = np.zeros(n)
for k in range(0,n):
    t[k] = te*k



"""
plot(t,data)   #trace le signal discretisé
xlabel("t (s)")
ylabel("amplitude")
show()
"""

#remarque : d'après ce que j'ai compris, data est une liste de 2-uplets représentants chacun l'information sur les deux pistes G et D droite à un instant donné. J'essaye ici de les extraire
"""
L = []
R = []
for i in range(n) :
    L.append(data[i][0])
    R.append(data[i][0])

plot(t,L)
show()   #ca marche
"""






"""
Analyse spectrale par transformation de Fourrier
"""

"""
def tracerSpectre(data,rate,debut,duree):
    start = int(debut*rate)
    stop = int((debut+duree)*rate)
    spectre = np.absolute(fft(data[start:stop]))
    spectre = spectre/spectre.max()
    n = spectre.size
    freq = np.zeros(n)
    for k in range(n):
        freq[k] = 1.0/n*rate*k
    vlines(freq,[0],spectre,'r')
    xlabel('f (Hz)')
    ylabel('A')
    axis([0,0.5*rate,0,1])
"""


"""
figure(figsize=(12,4))
tracerSpectre(data,rate,0.0,duree)

show()
"""


def corr(L,M,n) :  #les deux listes doivent avoir la même taille n ! Cette fonction donne la somme des ecarts en valeur absolue entre L[i] et M[j]
    ecart = 0
    for i in range(n) :
        ecart += abs(L[i]-M[i])
    return ecart

L = [0,0,0,0]
M = [1,0,3,-1]

print(corr(L,M,4))   #petit test, ca fonctionne
