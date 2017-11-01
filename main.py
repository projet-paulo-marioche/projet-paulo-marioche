import math
import numpy as np
from matplotlib.pyplot import *
import scipy.io.wavfile as wave
from numpy.fft import fft
from list import *


"""
Ouverture du fichier .wav, représentation temporelle
"""
tolerance = 5

fe,data = wave.read('loop_batterie.wav')   #fe = frequence d'échantillonage, déjà intégrée dans le fichier .wav
n = len(data)                #nombre d'échantillons
duree = 1.0*n/fe

print(fe)

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


L_comp,new_fe = compress(L,fe,100)

E = extract(L_comp,new_fe,10)    #extrait de la 2s à partir du milieu de la piste gauche





filter_E = filter(E,0.9)




scores = scores(filter_E)[500:]   #on enlève les premiers termes pour ne pas que la distance minimale soit donné par les faibles décalages du début

tempo = 60.0*new_fe/(min_index(scores)+500)     #est censé donner le tempo



print(right_tempo(tempo))  #permet de donner un multiple du tempo compris entre 60 et 120 bpm
