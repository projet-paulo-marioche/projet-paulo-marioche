import math
import numpy as np
from matplotlib.pyplot import *
import scipy.io.wavfile as wave
from numpy.fft import fft
from list import *


"""
Ouverture du fichier .wav, représentation temporelle
"""

fe,data = wave.read('loop_batterie.wav')   #fe = frequence d'échantillonage, déjà intégrée dans le fichier .wav
n = len(data)                #nombre d'échantillons
duree = 1.0*n/fe



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






L_comp,new_fe = compress(L,fe,10)

E = extract(L_comp,new_fe,2)    #extrait de la 2s à partir du milieu de la piste gauche

M = max(E)



filter_E =[]

for i in E :
    if i > 0.2*M :
        filter_E.append(i)
    else :
        filter_E.append(0)   #idée : si un échantillon n'est pas significatif, on le met à 0



scores = scores(filter_E)[500:]   #on enlève les premiers termes pour ne pas que la distance minimale soit donné par les petits décalages du début

tempo = 60.0*new_fe/(min_index(scores)+500)     #est censé donner le tempo

if tempo > 60 and tempo <130 :                  # la fin du script permet de donner un multpiple du tempo compris entre 60 et 120 bpm
    print(tempo)
elif tempo < 60 :
    while tempo <60 :
        tempo *= 2
    print(tempo)
else :
    while tempo > 130 :
        tempo = tempo/2
    print(tempo)
