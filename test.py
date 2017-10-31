import math
import numpy as np
from matplotlib.pyplot import *
import scipy.io.wavfile as wave
from numpy.fft import fft
from list import *


"""
Ouverture du fichier .wav, représentation temporelle
"""

fe,data = wave.read('loop_batterie.wav')   #rate = frequence d'échantillonage, déjà intégrée dans le fichier .wav
n = len(data)                #nombre d'échantillons
duree = 1.0*n/fe
print(n)


te = 1.0/fe
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

L = []
R = []
for i in range(n) :
    L.append(data[i][0])
    R.append(data[i][0])



"""
plot(t,L)
show()   #ca marche
"""

L_comp,new_fe = compress(L,fe,10)

E = extract(L_comp,new_fe,3)    #extrait de la 2s à partir du milieu de la piste gauche



scores = scores(E)[500:]

print(min_index(scores))
